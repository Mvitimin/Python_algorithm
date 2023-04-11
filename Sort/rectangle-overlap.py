from typing import List

class Solution:
	def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
		x1, y1, x2, y2 = rec1
		a1, b1, a2, b2 = rec2
		
		width = min(x2, a2) - max(a1, x1)
		height = min(y2, b2) - max(y1, b1)
		return (width > 0 and height > 0)

a = Solution()
rec1 = [0,0,2,2]; rec2 = [1,1,3,3]
rec1 = [0,0,1,1]; rec2 = [1,0,2,1]
rec1 = [0,0,1,1]; rec2 = [2,2,3,3]

rec1 = [-382,-696,838,-517]
rec2 = [-110,-690,247,-209]
print(a.isRectangleOverlap(rec1, rec2))
