from typing import List

class Solution:
	def minCostClimbingStairs(self, cost: List[int]) -> int:
		cost.append(0)
		n = len(cost)
		dp = [float('inf')] * (n + 2)
		dp[-2] = dp[-1] = 0
		for i in range(n):
			dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]
		return dp[n - 1]	

a = Solution()
cost = [10,15,20]
cost = [1,100,1,1,1,100,1,1,100,1]
print(a.minCostClimbingStairs(cost))			
		

