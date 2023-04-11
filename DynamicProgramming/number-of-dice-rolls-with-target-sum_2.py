from functools import lru_cache

class Solution:
	def numRollsToTarget(self, n: int, k: int, target: int) -> int:
		MODULO = 10 ** 9 + 7
		dp = [[0] * (target + 1) for _ in range(n + 1)]
		
		for i in range(1, min(k, target) + 1):
			dp[1][i] = 1
		
		for i in range(2, n + 1):
			for t in range(1, target + 1):
				for j in range(min(k, t), 0, -1):
					dp[i][t] += (dp[i - 1][t - j])
					dp[i][t] %= MODULO
		return dp[n][target]
		
a = Solution()
#n = 2; k = 6; target = 7
n = 30; k = 30; target = 500
#n = 1; k = 6; target = 3
print(a.numRollsToTarget(n, k, target))
