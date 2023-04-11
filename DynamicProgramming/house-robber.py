from typing import List

class Solution:
	def rob(self, nums: List[int]) -> int:
		if not nums:
			return 0
		if len(nums) <= 2:
			return max(nums) 
		dp = [nums[0], max(nums[0], nums[1])]
		for i in range(2, len(nums)):
			dp.append(max(dp[-2] + nums[i], dp[-1]))
		return dp[-1]
		
a = Solution()
nums = [2,1,1,2]
#nums = []
#nums = [1, 2, 3, 1]
print(a.rob(nums))

