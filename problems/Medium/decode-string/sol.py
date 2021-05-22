from typing import List

class Solution:
	def decodeString(self, s: str) -> str:
		i = 0
		flag = 0
		arr = []
		depth = 0
		charStr, numStr, repeatStr = "", "", ""
		while i < len(s):
			if flag == 0 and s[i].isdigit():
				if charStr:
					arr.append(charStr)
					charStr = ""
				flag = 1
				numStr = s[i]
			elif flag == 1 and s[i].isdigit():
				numStr += s[i]
			elif flag == 1 and s[i] == '[':
				flag = 2
				depth = 1
			elif flag == 2 and depth == 1 and s[i] == ']':
				depth = 0
				flag = 0
				arr.append((numStr, repeatStr))
				numStr = ""
				repeatStr = ""
			elif flag == 2:
				repeatStr += s[i]
				if s[i] == '[':
					depth += 1
				elif s[i] == ']':
					depth -= 1
			elif flag == 0:
				charStr += s[i]
			i += 1

		if charStr:
			arr.append(charStr)

		ans = ""
		for segment in arr:
			if isinstance(segment, tuple):
				ans += int(segment[0])*self.decodeString(segment[1])
			else:
				ans += segment
		return ans

print(Solution().decodeString("2[a3[2[t]b]c]3[cd]ef"))


