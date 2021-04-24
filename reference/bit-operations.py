from typing import List

class Solution:
	def toHex(self, num: int) -> str:
		def myHex(n):
			if n > 15:
				raise Exception("Overflow")
			elif 10 <= n <= 15:
				return chr(ord('a') + (n-10))
			elif n >= 0:
				return str(n)
			else:
				raise Exception("Underflow")


		def twoComplement(num: int) -> int:
			return (1 << 32) - num

		if num < 0:
			return self.toHex(twoComplement(-num))
		elif num >= 16:
			return self.toHex(num//16) + myHex(num%16)
		else:
			return myHex(num%16)


print(Solution().toHex(0))