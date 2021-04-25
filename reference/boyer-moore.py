def majorityElement(nums, k):
	d = {}
	for num in nums:
		if num in d:
			d[num] += 1
		elif num not in d and len(d) < k - 1:
			d[num] = 1
		elif num not in d and len(d) == k - 1:
			for key in d:
				d[key] -= 1
			d = {key: value for key, value in d.items() if value != 0}
	return [key for key in d.keys() if nums.count(key) > len(nums) // k]