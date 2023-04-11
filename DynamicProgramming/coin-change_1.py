from typing import List
class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		n = len(coins)
		dp = [float('inf')] * (amount + 1)
		coins.sort()
		dp[0] = 0
		for i in range(1, amount + 1):
			for val in coins:
				if i - val >= 0:
					dp[i] = min(dp[i], 1 + dp[i - val])
		return dp[amount] if dp[amount] != float('inf')	else -1		
		
a = Solution()
coins = [1,2,5]; amount = 11
coins = [1]; amount = 0
coins = [2]; amount = 3
coins = [1, 1, 3, 4]; amount = 7
print(a.coinChange(coins, amount))
