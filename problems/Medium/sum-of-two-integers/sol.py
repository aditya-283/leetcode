from typing import List

class Solution:
	def getSum(self, a: int, b: int) -> int:
		# this solution is fucking insane
		def getPadded64Bitstring(a):
			if a > 0:
				string = '{0:b}'.format(a)
				return '0'*(64-len(string)) + string
			else:
				string = '{0:b}'.format(-a)
				pos = '0'*(64-len(string)) + string
				s = ''
				for bit in pos:
					s += str(int(not (int(bit))))
				return addBitstrings(s, '0'*63 + '1')

		def to_integer(bitstring):
			if bitstring[0] == '1':
				s = ''
				bitstring = addBitstrings(bitstring, '1'*64)
				for bit in bitstring:
					s += str(int(not (int(bit))))
				return -1*int(s, 2)
			else:
				return int(bitstring, 2)


		def addBitstrings(a:str, b:str) -> str:
			a, b = a[::-1], b[::-1]
			s = ''
			carry = 0
			for b1, b2 in zip(a,b):
				b1, b2 = int(b1), int(b2)
				sum = b1 ^ b2 ^ carry
				carry = (not sum and (b1 or b2 or carry)) or (b1 and b2 and carry)
				s += str(sum)
			return s[::-1][:64]

		
		# 32 bit mask in hexadecimal
		mask = 0xffffffff
		
		# works both as while loop and single value check 
		while (b & mask) > 0:
			
			carry = ( a & b ) << 1
			a = (a ^ b) 
			b = carry
		
		# handles overflow
		return (a & mask) if b > 0 else a
		# return to_integer(addBitstrings(getPadded64Bitstring(a), getPadded64Bitstring(b)))

print(Solution().getSum(-2198, 1002))