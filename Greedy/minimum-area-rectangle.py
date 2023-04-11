from typing import List
import collections

class Solution:
	def minAreaRect(self, points: List[List[int]]) -> int:
		n = len(points)
		ans = float('inf')
	
		pointSet = set()
		for x, y in points:
			pointSet.add((x, y))	
		
		points.sort()
		
		for i in range(n):
			px1, py1 = points[i]
			for j in range(i + 1, n):
				px2, py2 = points[j]
				w, h = px2 - px1, py2 - py1		
				if w * h == 0: 
					continue
				if (px1 + w, py1) in pointSet and (px1, py1 + h) in pointSet:
					ans = min(ans, abs(w * h))
			
		return ans if ans != float('inf') else 0
		
a = Solution()
points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
#points = [[0,1],[1,3],[3,3],[4,4],[1,4],[2,3],[1,0],[3,4]]
#points = [[0,1],[3,2],[4,4],[0,2],[4,3],[2,4],[4,2],[1,1]]
#points = [[1,2],[1,3],[3,3],[4,4],[2,1],[1,4],[2,2],[1,0],[0,2]]


print(a.minAreaRect(points))
		
