from typing import List

class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		n = len(heights)
		ans = 0
		stack = []
		for i, h in enumerate(heights):
			j = i
			while stack and stack[-1][1] > h:
				j, height = stack.pop()
				ans = max(ans, (i - j) * height)
			stack.append((j, h))	
		for i, h in stack:
			ans = max(ans, (n - i) * h)
		return ans

a = Solution()
heights = [2,1,5,6,2,3]
#heights = [2,4]
print(a.largestRectangleArea(heights))
