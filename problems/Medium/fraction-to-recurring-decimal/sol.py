from typing import List

class Solution:
	def fractionToDecimal(self, numerator: int, denominator: int) -> str:
		def getFractionalPart(num, denom) -> str:
			rems = []
			quots = []

			recurring = None
			while True:
				# print(rems, quots, num)
				quot = 10*num // denom
				rem = 10*num % denom
				quots.append(str(quot))
				if not rem:
					recurring = 0
					break
				if num in rems:
					recurring = 1
					break
				rems.append(num)
				num = rem
			if not recurring:
				return ''.join(quots)
			else:
				idx = rems.index(rem)
				quots.insert(idx, '(')
				# quots = quots[:-1]
				quots.append(')')
				return ''.join(quots)

		if numerator*denominator < 0:
			return '-' + self.fractionToDecimal(-numerator, denominator)
		integerPart = numerator // denominator
		if numerator % denominator == 0:
			return str(integerPart)
		else:
			return str(integerPart) + '.' + getFractionalPart(numerator%denominator, denominator)


print(Solution().fractionToDecimal(-50, 8))