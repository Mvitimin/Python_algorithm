from typing import List
class Solution:
	def combinationSum4(self, nums: List[int], target: int) -> int:
		dp = [0] * (target + 1)
		dp[0] = 1
		for j in range(1, target + 1):
			for num in nums:
				if j - num >= 0:
					dp[j] += (dp[j - num])
		return dp[-1]
		
a = Solution()
#nums = [1,2,3]; target = 4			
nums = [9]; target = 3	
print(a.combinationSum4(nums, target))
