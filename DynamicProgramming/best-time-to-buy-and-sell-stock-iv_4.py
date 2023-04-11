from typing import List

class Solution:
	def maxProfit(self, k: int, prices: List[int]) -> int:
		if k == 0 or not prices:
			return 0	
		n = len(prices)
				
		dp = [[[float('-inf')] * 2 for _ in range(k + 1)] for _ in range(n)]
		dp[0][0][0] = 0
		dp[0][1][1] = -prices[0]
		for i in range(1, n):
			for j in range(k + 1):
				dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
				if j > 0:
					dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])	
		return max(dp[-1][j][0] for j in range(k + 1))

a = Solution()
k = 3; prices = [2,4,1]
k = 2; prices = [1,2,4]
k = 4; prices = [1,2,4,2,5,7,2,4,9,0]
#k = 2; prices = [3,2,6,5,0,3]
#k = 2; prices = []
print(a.maxProfit(k, prices))
