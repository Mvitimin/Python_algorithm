from typing import List
from functools import lru_cache
class Solution:
	def minCostClimbingStairs(self, cost: List[int]) -> int:
		n = len(cost)
		@lru_cache(None)
		def dp(i):
			if i >= n:
				return 0
			return cost[i] + min(dp(i + 1), dp(i + 2))
		return min(dp(0), dp(1))

a = Solution()
cost = [10,15,20]
#cost = [1,100,1,1,1,100,1,1,100,1]
print(a.minCostClimbingStairs(cost))	
