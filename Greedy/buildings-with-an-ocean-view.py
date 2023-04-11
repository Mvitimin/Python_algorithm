from typing import List

class Solution:
	def findBuildings(self, heights: List[int]) -> List[int]:
		max_height = 0
		ans = []
		for i in range(len(heights) - 1, -1, -1):
			if heights[i] > max_height:
				ans.append(i)
			max_height = max(max_height, heights[i])
		return list(reversed(ans))


a = Solution()
heights = [4,2,3,1]
heights = [4,3,2,1]
heights = [1,3,2,4]
heights = [2,2,2,2]
print(a.findBuildings(heights))
