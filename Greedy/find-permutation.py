from typing import List
class Solution:
	def findPermutation(self, s: str) -> List[int]:
		n = len(s)
		j = 1
		stack = [0]
		res = [1] * (n + 1)
		for i, c in enumerate(s):
			if c == 'I':
				while stack:
					res[stack.pop()] = j
					j += 1 
			stack.append(i + 1)
		while stack:
			res[stack.pop()] = j 
			j += 1	
		return res	

a = Solution()
s = "DI"
s = "DDIID"
s = "IIDD"
s = "DDIIDID"
#s = "D"
print(a.findPermutation(s))
		
		


