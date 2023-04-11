from typing import List

class Solution:
	def findMinArrowShots(self, points: List[List[int]]) -> int:
		n = len(points)
		stack = []
		points.sort(key = lambda x : x[1])
		for xs, xe in points:
			if not stack or stack[-1] < xs:
				stack.append(xe)
		return len(stack)

a = Solution()
points = [[10,16],[2,8],[1,6],[7,12]]
#points = [[1,2],[3,4],[5,6],[7,8]]
#points = [[1,2],[2,3],[3,4],[4,5]]
#points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
print(a.findMinArrowShots(points))				
			
		
