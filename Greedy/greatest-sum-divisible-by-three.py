from typing import List
class Solution:
	def maxSumDivThree(self, nums: List[int]) -> int:
		n = len(nums)
		dp = [[0] * 3 for _ in range(n + 1)]
		for i in range(n):
			for j in range(3):
				x = (dp[i - 1][j] + nums[i])
				dp[i][x % 3] = max(x, dp[i][x % 3])
				dp[i][j] = max(dp[i - 1][j], dp[i][j])
		return dp[n - 1][0] 
			
			
					
			
						
			
			
		
		

a = Solution()
nums = [3,6,5,1,8]
#nums = [1,2,3,4,4]
nums = [4]
#nums = [2, 6, 2, 2, 7]
print(a.maxSumDivThree(nums))
