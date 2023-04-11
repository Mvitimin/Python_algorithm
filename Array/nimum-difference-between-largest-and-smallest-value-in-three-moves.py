from typing import List
import collections
class Solution:
	def minDifference(self, nums: List[int]) -> int:
		if len(nums) <= 4:
			return 0
		nums.sort()
		start, end = 3, len(nums) - 1
		diff = float('inf')
		while start >= 0 and start <= end:
			print(start, end)
			diff = min(diff, nums[end] - nums[start])
			start -= 1
			end -= 1
		return diff
		
a = Solution()
nums = [5,3,2,4]
nums = [1,5,0,10,14]
print(a.minDifference(nums))
