# https://leetcode.com/explore/interview/card/google/59/array-and-strings/3048/
from typing import List

class Solution:
	def maxArea(self, height: List[int]) -> int:
		left, right = 0, len(height) - 1
		max_area, area = 0, 0
		
		while left < right:
			if height[left] <= height[right]:
				area = (right - left) * height[left]
				left += 1
			else:
				area = (right - left) * height[right]
				right -= 1
			max_area = max(max_area, area)
		return max_area		
		
a = Solution()
#height = [1,8,6,2,5,4,8,3,7]
#height = [1,1]
#height = [4,3,2,1,4]
height = [1,2,1]
print(a.maxArea(height))		
