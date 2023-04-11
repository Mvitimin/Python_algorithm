from typing import List

class Solution:
	def canJump(self, nums: List[int]) -> bool:
		n = len(nums)
		i, end = 0, nums[0]
		while i <= end:
			end = max(i + nums[i], end)
			if end >= n - 1:
				return True
			i += 1	
		return False

a = Solution()
nums = [2,3,1,1,4]
#nums = [3,2,1,0,4]
#nums = [2, 0]
nums = [1, 2, 3]
#nums = [2, 5, 0, 0]
print(a.canJump(nums))
