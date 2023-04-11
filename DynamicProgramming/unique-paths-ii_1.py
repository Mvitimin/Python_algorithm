from typing import List

class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
		m, n = len(obstacleGrid), len(obstacleGrid[0])
		dp = [[0] * (n + 1) for _ in range(m + 1)]
		dp[0][0] = 0 if obstacleGrid[0][0] else 1
		for i in range(m):
			for j in range(n):
				if (i == 0 and j == 0) or obstacleGrid[i][j]:
					continue
				dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
		return dp[m - 1][n - 1]
		
a = Solution()
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
obstacleGrid = [[0,1],[0,0]]
print(a.uniquePathsWithObstacles(obstacleGrid))		
				
				

