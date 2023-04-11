from typing import List
import collections
class Solution:
	def findTargetSumWays(self, nums: List[int], target: int) -> int:
		n = len(nums)
		dp = [[0] * 2001 for _ in range(n + 1)]
		dp[n][target] = 1
		for i in range(n - 1, -1, -1):
			for j in range(-1000, 1001):
				dp[i][j] = dp[i + 1][j + nums[i]] + dp[i + 1][j - nums[i]]
		return dp[0][0]	
					
a = Solution()
nums = [1,1,1,1,1]; target = 3
nums 
nums = [1]; target = 1
print(a.findTargetSumWays(nums, target))
			
