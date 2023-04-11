from typing import List

class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
		m, n = len(obstacleGrid), len(obstacleGrid[0])
		dp = [[0] * (n + 1) for _ in range(m + 1)]
		dp[1][0] = 1
		for i in range(1, m + 1):
			for j in range(1, n + 1):
				if obstacleGrid[i - 1][j - 1] != 1:
					dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
					
		return dp[m][n]

a = Solution()
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
obstacleGrid = [[0,1],[0,0]]
print(a.uniquePathsWithObstacles(obstacleGrid))
