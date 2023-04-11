class Solution:
	def decodeString(self, s: str) -> str:
		n = len(s)
		i = 0
		
		digits = []
		ans = []
		stack = []
		
		while i < n:
			if s[i].isdigit():
				start = i
				while s[i + 1].isdigit():
					i += 1
				digits.append(int(s[start:i + 1]))
			elif s[i] == '[': 
				stack.append('')		
			elif s[i] == ']':
				t = stack.pop() * digits.pop()
				if stack:
					stack[-1] += t	
				else:
					ans.append(t)						
			else:
				if not stack:
					ans.append(s[i])
				else:
					stack[-1] += s[i]
			i += 1
		return ''.join(ans)	
				
				
				
								
a = Solution()
s = "3[a]2[bc]"
#s = "3[a2[c]]"
#s = "2[abc]3[cd]ef"
#s = "1[a2[b2[c]]]"
#s = "12[abcd]"
#s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
print(a.decodeString(s))
#print('hi' * 2)
