from typing import List

class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		dp, n = {0: 0}, len(coins)
		def solve(total):
			if total in dp:
				return dp[total]
			dp[total] = float('inf')
			for i in range(n):
				if total - coins[i] >= 0:
					dp[total] = min(dp[total], 1 + solve(total - coins[i]))			
			return dp[total]
		return dp[amount] if solve(amount) != float('inf') else -1

a = Solution()
coins = [1,2,5]; amount = 11
#coins = [1]; amount = 0
#coins = [2]; amount = 3
#coins = [1, 1, 3, 4]; amount = 7
print(a.coinChange(coins, amount))

