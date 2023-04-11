from typing import List

class Solution:
	def PredictTheWinner(self, nums: List[int]) -> bool:
		n = len(nums)
		dp = [[0] * (n) for _ in range(n + 1)]
		for i in range(n - 1, -1, -1):
			for j in range(i, n):
				dp[i][j] = max(nums[i] - dp[i + 1][j], 
				nums[j] - dp[i][j - 1])
		
		return dp[0][n - 1] >= 0 


a = Solution()
#nums = [1,5,2]
nums = [1,5,233,7]
print(a.PredictTheWinner(nums))
