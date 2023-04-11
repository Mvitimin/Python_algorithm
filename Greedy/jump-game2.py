from typing import List
import collections

class Solution:
	def canJump(self, nums: List[int]) -> bool:
		if len(nums) < 2:
			return True
		start = len(nums) - 1
		for i in range(len(nums) - 1, -1, -1):
			start = min(start, i - nums[i])
		return True if start <= 0 else False
				
nums = [2,3,1,1,4]		
#nums = [3,2,1,0,4]
#nums = [3,3,1,2,5,6,7,8,9,1,2,3,4]
#nums = [1,1,1,0]
a = Solution()
print(a.canJump(nums))
