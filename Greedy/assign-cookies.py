from typing import List

class Solution:
	def findContentChildren(self, g: List[int], s: List[int]) -> int:
		ans = 0
		g.sort()
		s.sort()
		while len(g) and len(s):
			if g[-1] <= s[-1]:
				g.pop()
				s.pop()
				ans += 1
			else:
				g.pop()
		return ans
		
		
a = Solution()
g = [1,2]
s = [1,2,3]
print(a.findContentChildren(g, s))
