from typing import List


# DON'T USE SPLIT AND JOIN AT ALL. It could have been elegant but the edge cases make it not so.
# [len]S is still the best way I think, although yes it requires a custom parser



# Certified shit
class Codec:
	def encode(self, strs: [str]) -> str:
		"""Encodes a list of strings to a single string.
		"""
		if len(strs) == 1 and not strs[0]:
			return 'singleempty'
		maxLength = max([len(s) for s in strs]) if strs else 0
		valid_stop = ' ' + ('#' * (maxLength + 1)) + ' '
		return valid_stop.join(strs)



		

	def decode(self, s: str) -> [str]:
		"""Decodes a single string to a list of strings.
		"""
		def longestConsecutive(s, c):
			flag = 0
			max_len, l = 1, 0
			for char in s:
				if flag == 0 and char == c:
					flag = 1
					l += 1
				elif flag == 1 and char == c:
					l += 1
					max_len = max(l, max_len)
				elif flag == 1 and char != c:
					flag = 0
					l = 0
			return max_len

		if not s:
			return []

		if s == 'singleempty':
			return ['']

		stop = ' ' + '#'*longestConsecutive(s, '#') + ' '
		arr = s.split(stop)
		return arr
		



# Your Codec object will be instantiated and called as such:
codec = Codec()
arr = []
# print(codec.encode(arr))
print(codec.decode(codec.encode(arr)))
 #  # 


# [] -> []
# ['']
# ['', '']
# ['', 'aa', '']