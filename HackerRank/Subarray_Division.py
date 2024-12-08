def birthday(s,d,m):
	ans = 0
	c = 0
	chunks = []
	
	while c <= len(s) -1:
		chunk = []
		for x in range(m):
			if 0 <= (c+x) < len(s):
				chunk.append(s[c+x])
			
		chunks.append(chunk)		
		c += 1
	
	for i in chunks:
		if len(i) == m and sum(i) == d:
			ans += 1
			
	return ans


# -----------------

s = [4]
d = 4
m = 1

solution = birthday(s,d,m)
print(f'--> {solution}')
