from typing import List
from collections import defaultdict

class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		anagrams = defaultdict(list)
		for string in strs:
			anagrams[''.join(sorted(string))].append(string)
		return list(anagrams.values())

print(Solution().groupAnagrams(['tea', 'ate', 'eat', 'pot', 'top', 'cry', 'ryc']))