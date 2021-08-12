def encodeRLE(s):
	ans = ''
	cnt = 0
	n = len(s)
	for i in range(n):
		if i == 0:
			cnt = 1
		elif s[i] == s[i-1]:
			cnt += 1
		else:
			ans += f'{cnt}{s[i-1]}'
			cnt = 1
	ans += f'{cnt}{s[n-1]}'
	print(ans)
	return ans

# a = encodeRLE('aaaabbbccc')



# def decodeRLE(s):
# 	n = len(s)
# 	if n % 2:
# 		print("Invalid string")
# 		return ''
# 	elif not all(s[i].isdigit() and s[i+1].isalpha() for i in range(n) if not i%2):
# 		print("Invalid string")
# 		return ''

# 	ans = ''
# 	for i in range(0, n, 2):
# 		ans += s[i+1]*int(s[i])
# 	return ans

# print(decodeRLE("3a5g2a"))