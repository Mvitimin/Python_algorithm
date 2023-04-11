from typing import List

class Solution:
	def maxDistance(self, arrays: List[List[int]]) -> int:
		max1 = arrays[0][-1]
		min1 = arrays[0][0] 
		diff = float('-inf')
		for i in range(1, len(arrays)):
			diff = max(diff, arrays[i][-1] - min1, max1 - arrays[i][0])
			min1 = min(min1, arrays[i][0])
			max1 = max(max1, arrays[i][-1])
		return diff
			
			
a = Solution()
arrays = [[1,2,3],[4,5],[1,2,3]]
#arrays = [[1],[1]]
#arrays = [[1,4],[0,5]]
print(a.maxDistance(arrays))
