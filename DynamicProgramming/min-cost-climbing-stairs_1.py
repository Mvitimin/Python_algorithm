from typing import List
class Solution:
	def minCostClimbingStairs(self, cost: List[int]) -> int:
		n = len(cost)
		dp = [0] * (n)
		for i in range(n):
			dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
		return min(dp[-1], dp[-2])

a = Solution()
cost = [10,15,20]
#cost = [1,100,1,1,1,100,1,1,100,1]
print(a.minCostClimbingStairs(cost))	
