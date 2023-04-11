import collections

class Solution:
	def calculate(self, s: str) -> int:
		q = collections.deque([])
		op = set(['+', '-', '*', '/'])
		s = s.replace(' ', '')
		def calc(a, operator, b):
			if operator == '+':
				return a + b
			elif operator == '-':
				return a - b
			elif operator == '*':
				return a * b
			else:
				return a // b
	
		n = len(s); k = 0
		for i, c in enumerate(s):
			if c.isdigit():
				if q and q[-1] in ['*', '/']:
					k = k * 10 + int(c)
					if i == n - 1 or (i < n - 1 and not s[i + 1].isdigit()):
						operator = q.pop()
						q[-1] = calc(q[-1], operator, k)
						k = 0						
				elif q and q[-1] not in ['+', '-']:
					q[-1] = q[-1] * 10 + int(c)
				else:
					q.append(int(c))
			else:
				q.append(c)
		
		while len(q) >= 3:
			a = q.popleft()
			operator = q.popleft()
			q[0] = calc(a, operator, q[0])
		
		return q[0]
		
a = Solution()
s = "3+2*2"
s = "3/2"
s = " 3+5 / 2"
s = "1-1+1"
s = "0-2147483647"
s = "1*2-3/4+5*6-7*8+9/10"
s = "1"
print(a.calculate(s))
