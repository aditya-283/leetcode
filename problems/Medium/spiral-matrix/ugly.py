class Solution:
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		min_x, max_x = 0, len(matrix[0]) - 1
		min_y, max_y = 0, len(matrix) - 1
		cur_x, cur_y = min_x, min_y
		phase = 1
		spiral = [matrix[cur_y][cur_x]]
		if len(matrix) == 1:
			return matrix[0]
		if len(matrix[0]) == 1:
			return [l[0] for l in matrix]
		while True:
			if phase == 1:
				if  cur_x < max_x:
					cur_x += 1
				elif cur_x == max_x:
					min_y += 1
					cur_y += 1
					phase = 2
				else:
					break
			elif phase == 2:
				if cur_y < max_y:
					cur_y += 1
				elif cur_y == max_y:
					max_x -= 1
					cur_x -= 1
					phase = 3
				else: 
					break
			elif phase == 3:
				if cur_x > min_x:
					cur_x -= 1
				elif cur_x == min_x:
					max_y -= 1
					cur_y -= 1
					phase = 4
				else:
					break
			elif phase == 4:
				if cur_y > min_y:
					cur_y -= 1
				elif cur_y == min_y:
					min_x += 1
					cur_x += 1
					phase = 1
				else:
					break
			spiral.append(matrix[cur_y][cur_x])
		return spiral[:-1]

