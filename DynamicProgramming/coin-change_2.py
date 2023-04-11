from typing import List
class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		n = len(coins)
		dp = [float('inf')] * (amount + 1)
		dp[0] = 0
		
		for i in range(n):
			for j in range(amount):
				if j + coins[i] <= amount:
					dp[j + coins[i]] = min(dp[j + coins[i]], dp[j] + 1)
		return -1 if dp[-1] == float('inf') else dp[-1]
	
a = Solution()
coins = [1,2,5]; amount = 11
coins = [2]; amount = 3
coins = [1]; amount = 0
print(a.coinChange(coins, amount)) 
