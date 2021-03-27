from typing import List


class Solution:
	def addStrings(self, num1: str, num2: str) -> str:
		carry = 0
		sum = []

		l1, l2 = len(num1), len(num2)
		if l2 < l1:
			num2 = '0'*(l1-l2) + num2
		else:
			num1 = '0'*(l2-l1) + num1

		for i, j in zip(num1[::-1], num2[::-1]):
			x, y = int(i), int(j)
			s = (x + y + carry)
			carry = s // 10
			sum.append(str(s % 10))

		if carry:
			sum.append(str(carry))
		return ''.join(sum[::-1])


print(Solution().addStrings('1', '9'))