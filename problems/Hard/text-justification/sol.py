from typing import List

class Solution:
	def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
		lines = []
		chars = 0
		line = []
		ans_lines = []
		for word in words:
			# print(word, line, chars)
			if chars + len(word) <= maxWidth:
				line.append(word)
				chars += len(word) + 1
			else:
				lines.append(line)
				line = [word]
				chars = len(word) + 1
		lines.append(line)
		# print(lines)
		for line in lines[:-1]:
			breaks = maxWidth - sum(len(w) for w in line)
			if len(line) == 1:
				ans_lines.append(line[0] + " "*breaks)
			else:
				common = breaks // (len(line) - 1)
				rem = breaks % (len(line) - 1)
				ans_line = ""
				for i in range(len(line)):
					ans_line += line[i]
					if i < rem:
						ans_line += " "*(common + 1)
					elif i < len(line) - 1:
						ans_line += " "*common
				ans_lines.append(ans_line)
		ans_lines.append(" ".join(lines[-1]))
		ans_lines[-1] = ans_lines[-1] + " "*(maxWidth - len(ans_lines[-1]))
		# print([len(line) for line in ans_lines])
		return ans_lines

print(Solution().fullJustify(words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20))