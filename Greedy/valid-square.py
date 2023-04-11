from typing import List
import math
class Solution:
	def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
		
		cases = [[(p1, p2), (p3, p4)], [(p1, p3), (p2, p4)], [(p1, p4), (p2, p3)]]
		
		def center(d1, d2):
			return ((d1[0] + d2[0]) / 2, (d1[1] + d2[1]) / 2)
		
		def length(d1, d2):
			return math.sqrt((d1[0] - d2[0]) ** 2 + (d1[1] - d2[1]) ** 2)
		
		for g1, g2 in cases:
			c1x, c1y = center(g1[0], g1[1])
			c2x, c2y = center(g2[0], g2[1])
			l1, l2 = length(g1[0], g2[0]), length(g1[1], g2[0])
			a1, a2 = length(g1[0], g1[1]), length(g2[0], g2[1])
			if c1x == c2x and c1y == c2y and l1 == l2 and a1 == a2 and l1: return True
		return False

a = Solution()
p1 = [0,0]; p2 = [1,1]; p3 = [1,0]; p4 = [0,1]
p1 = [0,0]; p2 = [1,1]; p3 = [1,0]; p4 = [0,12]
p1 = [1,0]; p2 = [-1,0]; p3 = [0,1]; p4 = [0,-1]
print(a.validSquare(p1, p2, p3, p4))

		
