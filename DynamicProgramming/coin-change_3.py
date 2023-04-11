from typing import List
from functools import lru_cache
class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		n = len(coins)
		
		@lru_cache(None)
		def dp(money):
			if money == 0: return 0
			val = float('inf')
			for j in range(n):
				if money - coins[j] >= 0:
					val = min(val, 1 + dp(money - coins[j]))
			return val	
		ans = dp(amount)
		return -1 if ans == float('inf') else ans
		
		
a = Solution()
coins = [1,2,5]; amount = 15
coins = [1]; amount = 0
#coins = [2]; amount = 3
coins = [1, 1, 3, 4]; amount = 7
print(a.coinChange(coins, amount))
