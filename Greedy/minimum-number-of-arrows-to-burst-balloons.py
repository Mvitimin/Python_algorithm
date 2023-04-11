from typing import List

class Solution:
	def findMinArrowShots(self, points: List[List[int]]) -> int:
		points.sort()
		stack = []
		for x, y in points:
			m = y 
			if stack and stack[-1] >= x:
				m = min(stack.pop(), m)
			stack.append(m)
		return len(stack)
		
	
a = Solution()
points = [[10,16],[2,8],[1,6],[7,12]]
points = [[1,2],[3,4],[5,6],[7,8]]
points = [[1,2],[2,3],[3,4],[4,5]]
print(a.findMinArrowShots(points))	
