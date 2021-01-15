class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []        # Triples
        n = len(nums)   # Length of the list
        nums.sort()     # We need to sort the list first!
        
        for i in range(n-2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0: # sum too small, move left ptr
                    l += 1
                elif s > 0: # sum too large, move right ptr
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    # we need to skip elements that are identical to our
                    # current solution, otherwise we would have duplicated triples.
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res