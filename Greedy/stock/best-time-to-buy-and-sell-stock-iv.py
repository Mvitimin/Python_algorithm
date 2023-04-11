from typing import List
class Solution:
	def maxProfit(self, k: int, prices: List[int]) -> int:
		if k == 0 or not prices:
			return 0
		n = len(prices)
		dp = [[[float('-inf')] * 2 for _ in range(k + 1)] for _ in range(n)]
		S, B = 0, 1
		dp[0][0][S] = 0
		dp[0][1][B] = -prices[0]
		for i in range(1, n):
			for j in range(k + 1):
				dp[i][j][S] = max(dp[i - 1][j][S], dp[i - 1][j][B] + prices[i])
				if j > 0:
					dp[i][j][B] = max(dp[i - 1][j][B], dp[i - 1][j - 1][S] - prices[i])
				
		return max(dp[-1][j][S] for j in range(k + 1))

a = Solution()
k = 2; prices = [3,2,6,5,0,3]
k = 1; prices = [2, 1]
#k = 2; prices = [4, 2, 1, 7]
k = 2; prices = [1,2,4]
print(a.maxProfit(k, prices))
			
	
				
'''
from typing import List
from functools import lru_cache
class Solution:
	def maxProfit(self, k: int, prices: List[int]) -> int:
		n = len(prices)
		B, S = 0, 1
		@lru_cache(None)
		def dp(i, cnt, status):
			if cnt <= 0 or i >= n: return 0
			val = dp(i + 1, cnt, status)
			if status == S:
				val = max(val, prices[i] + dp(i, cnt - 1, B))
			else:
				val = max(val, -prices[i] + dp(i, cnt, S))
			return val
		return dp(0, k, B)

a = Solution()
k = 2; prices = [3,2,6,5,0,3]
print(a.maxProfit(k, prices))
			
				
'''			
			
			
