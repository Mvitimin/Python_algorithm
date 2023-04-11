from typing import List

class Solution:
	def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
		
		n, m = len(nums), len(multipliers)
		dp = [[float('-inf')] * (m + 1) for _ in range(m)]
		dp += [[0] * (m + 1)]
		
		for k in range(m - 1, -1, -1):
			for i in range(k, -1, -1):
				j = n + i - 1 - k	
				dp[k][i] = max(nums[i] * multipliers[k] + dp[k + 1][i + 1], nums[j] * multipliers[k] + dp[k + 1][i])
				print(i, j, k)		
		return max(dp[0])		
					
a = Solution()
nums = [1,2,3]; multipliers = [3,2,1]
nums = [-5,-3,-3,-2,7,1]; multipliers = [-10,-5,3,4,6]
print(a.maximumScore(nums, multipliers))






