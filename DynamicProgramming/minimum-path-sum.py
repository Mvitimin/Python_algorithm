from typing import List

class Solution:
	def minPathSum(self, grid: List[List[int]]) -> int:
		m, n = len(grid), len(grid[0])
		dp = [[0] * (n + 1) for _ in range(m + 1)]
		for i in range(1, m + 1):
			for j in range(1, n + 1):
				dp[i][j] = grid[i - 1][j - 1]
				if i == 1:
					dp[i][j] += dp[i][j - 1]
				elif j == 1:
					dp[i][j] += dp[i - 1][j]
				else:
					dp[i][j] += min(dp[i][j - 1], dp[i - 1][j])
		return dp[m][n]

a = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
#grid = [[1,2,3],[4,5,6]]
print(a.minPathSum(grid))

