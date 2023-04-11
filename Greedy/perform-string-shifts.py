from typing import List

class Solution:
	def stringShift(self, s: str, shift: List[List[int]]) -> str:
		n = len(s)
		l_start = 0
		for d, amount in shift:
			if d == 0:
				l_start += amount
			else:
				l_start -= amount
		
		l_start %= n
		return s[l_start:] + s[:l_start]
		
a = Solution()
s = "abc"; shift = [[0,1],[1,2]]
#s = "abcdefg"; shift = [[1,1],[1,1],[0,2],[1,3]]
#s ="xqgwkiqpif"; shift =[[1,4],[0,7],[0,8],[0,7],[0,6],[1,3],[0,1],[1,7],[0,5],[0,6]]
#s = "abc"; shift = [[0, 4]]
print(a.stringShift(s, shift))		

print(-2% 3)
