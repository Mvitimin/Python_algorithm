from typing import List

class Solution:
	def findMinArrowShots(self, points: List[List[int]]) -> int:
		points.sort(key=lambda x : x[1])
		ans = 0
		pre_idx = -1
		for i, point in enumerate(points):
			start, end = point
			
			if pre_idx != -1 and points[pre_idx][1] >= start:
				continue
			else:
				pre_idx = i
				ans += 1
		return ans

			
						
a = Solution()
points = [[10,16],[2,8],[1,6],[7,12]]
#points = [[1,2],[3,4],[5,6],[7,8]]
#points = [[1,2],[2,3],[3,4],[4,5]]
#points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
print(a.findMinArrowShots(points))			
