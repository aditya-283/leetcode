from typing import List
from math import inf
from functools import cache

class Solution:
	def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
		@cache
		def shelfRec(i):
			if i == len(books):
				return 0
			j = i
			sum_ = books[i][0]
			while j + 1 < len(books) and sum_ + books[j+1][0] <= shelf_width:
				sum_ += books[j+1][0]
				j = j + 1
			
			ans = inf
			ht = 0
			for k in range(i, j+1):
				ht = max(ht, books[k][1])
				ans = min(ans, ht + shelfRec(k+1))
			return ans

		return shelfRec(0)

print(Solution().minHeightShelves(books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4))