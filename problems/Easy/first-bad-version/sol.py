from typing import List


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
	def firstBadVersion(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		def firstBadVersionBinSearch(left, right):
			mid = (left + right) // 2
			if isBadVersion(mid):
				if isBadVersion(mid-1):
					return firstBadVersionBinSearch(left, mid-1)
				else:
					return mid
			elif not isBadVersion(mid):
				return firstBadVersionBinSearch(mid+1, right)
				
		return firstBadVersionBinSearch(1, n)