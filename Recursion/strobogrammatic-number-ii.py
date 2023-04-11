from typing import List

class Solution:
	def findStrobogrammatic(self, n: int) -> List[str]:
		if n % 2 == 1:
			stack = ['1', '8', '0']
		else: stack = ['']
		
		for i in range(n // 2):
			tmp = []
			while stack:
				number = stack.pop()
				for j in [1, 8, 0, 9, 6]:
					if j in [9, 6]:
						s = ''.join(map(str, [j, number, 15 - j]))
					else: s = ''.join(map(str, [j, number, j]))
					tmp.append(s)
					if i == (n // 2 - 1) and int(tmp[-1]) < 10 ** (n - 1):
						tmp.pop()
			stack = tmp
		return stack
									
a = Solution()
print(a.findStrobogrammatic(3))

