from typing import List
class Solution:
	def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
		dp = [[[float('inf')] * n for _ in range(target + 1)]	for _ in range(m)]
		if houses[0] == 0:
			for i in range(n):
				dp[0][0][i] = cost[0][i] 
		else: dp[0][0][houses[0] - 1] = 0		
		for i in range(1, m):
			start = (houses[i] - 1) if houses[i] != 0 else 0
			for j in range(min(i + 1, target)):
				for k in range(start, n):
					dp[i][j][k] = dp[i - 1][j][k]	
					for h in range(n):
						if k != h:
							dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j - 1][h])
					if houses[i] != 0: break
					dp[i][j][k] += cost[i][k]
		ans = min(dp[-1][target - 1])
		return ans if ans != float('inf') else -1
houses = [0,0,0,0,0]; cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]; m = 5; n = 2; target = 3
#houses = [0,2,1,2,0]; cost = [[1,10],[10,1],[10,1],[1,10],[5,1]]; m = 5; n = 2; target = 3
#houses = [3,1,2,3]; cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]]; m = 4; n = 3; target = 3

#houses = [5,0,0,0,3,0,1,0,0,1,3,1,2,5];cost = [[4,19,5,10,14],[8,12,10,2,10],[14,20,6,9,11],[3,15,4,3,19],[8,4,3,2,16],[17,12,3,20,18],[2,1,18,6,7],[16,5,11,8,6],[9,8,6,3,8],[4,20,15,17,1],[5,15,16,16,12],[16,9,18,3,18],[12,9,16,8,15],[7,19,1,10,12]];m = 14;n = 5;target = 7

a = Solution()
print(a.minCost(houses, cost, m, n, target))
