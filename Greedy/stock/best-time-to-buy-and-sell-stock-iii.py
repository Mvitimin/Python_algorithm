from typing import List

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		n = len(prices)
		B, S = 1, 0
		dp = [[[float('-inf')] * 2 for _ in range(3)] for _ in range(n)]
		dp[0][1][B] = -prices[0]
		dp[0][0][S] = 0 
		k = 2
		for i in range(1, n):
			for j in range(k + 1):
				dp[i][j][S] = max(dp[i - 1][j][S], dp[i - 1][j][B] + prices[i])
				if j > 0:
					dp[i][j][B]= max(dp[i - 1][j][B], dp[i - 1][j - 1][S] - prices[i])
		return max(dp[-1][i][S] for i in range(k + 1))

a = Solution()
prices = [3,3,5,0,0,3,1,4]
prices = [1,2,3,4,5]
prices = [7,6,4,3,1]
prices = [1]
print(a.maxProfit(prices))
			
				

