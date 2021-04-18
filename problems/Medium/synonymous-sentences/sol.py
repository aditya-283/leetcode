from typing import List


class Solution:
	def doesCircleExist(commands):
		answers = []
		for command in commands:
			net_rotation = abs(command.count('L') - command.count('R'))
			if net_rotation == 0 and command.count('G') == 0:
				answers.append('YES')
			elif net_rotation == 0 and command.count('G') != 0:
				answers.append('NO')
			elif net_rotation % 4 != 0:
				answers.append('YES')
			else:
				answers.append('NO') 
		
from typing import List
