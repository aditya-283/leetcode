from typing import List

def to_binary(n: int) -> str:
	s = ''
	while n:
		s +=  str(n%2)
		n //= 2
	print(s)
	return s[::-1]


class Solution:
	def reverseBits(self, n: int) -> int:
		binary = to_binary(n)
		binary = '0'*(32-len(binary)) + binary
		return int(binary[::-1], 2)


# print(to_binary(8))
print(Solution().reverseBits(43261596))