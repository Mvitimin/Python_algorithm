from typing import List

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		n = len(prices)
		dp = [[float('-inf')] * 3 for _ in range(n)]
		
		dp[0][1] = -prices[0] # buy
		dp[0][0] = 0 # nothing
		dp[0][2] = 0 # sell
		for i in range(1, n):
			dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
			dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
			dp[i][0] = dp[i - 1][2]
		
		return dp[-1][2]

a = Solution()
prices = [1,2,3,0,2]
prices = [2, 1, 4]
print(a.maxProfit(prices))
