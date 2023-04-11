class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		dp = [[0] * (n + 1) for _ in range(m + 1)]	
		dp[0][0] = 1
		for i in range(m):
			for j in range(n):
				if i == 0 and j == 0: continue
				dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
		return dp[m - 1][n - 1]

a = Solution()
m = 3; n = 2
print(a.uniquePaths(m, n))	
				
