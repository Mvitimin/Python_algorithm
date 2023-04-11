from typing import List

class Solution:
	def maxKilledEnemies(self, grid: List[List[str]]) -> int:
		m, n = len(grid), len(grid[0])
		dp = [[[0] * 4 for _ in range(n + 1)] for _ in range(m + 1)]
		ans = 0
		
		for i in range(m):
			for j in range(n):
				if grid[i][j] != 'W':
					dp[i][j][0] = dp[i][j - 1][0] + (1 if grid[i][j] == 'E' else 0)
			for j in range(n - 1, -1, -1):
				if grid[i][j] != 'W':
					dp[i][j][1] = dp[i][j + 1][1] + (1 if grid[i][j] == 'E' else 0)
		
		for j in range(n):
			for i in range(m):
				if grid[i][j] != 'W':
					dp[i][j][2] = dp[i - 1][j][2] + (1 if grid[i][j] == 'E' else 0)
			for i in range(m - 1, -1 ,-1):
				if grid[i][j] != 'W':
					dp[i][j][3] = dp[i + 1][j][3] + (1 if grid[i][j] == 'E' else 0)
				if grid[i][j] == '0':
					ans = max(ans, dp[i - 1][j][2] + dp[i + 1][j][3] + dp[i][j - 1][0] + dp[i][j + 1][1])
		
		'''
		for i in range(m):
			print(dp[i])
		'''
		return ans
									
		
grid = [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"], ["0", "E", "0", "0"]]
#grid = [["W","W","W"],["0","0","0"],["E","E","E"]]
#grid = [["W","W","W","W","E"],["W","E","E","E","E"],["W","E","0","E","0"],["W","E","E","E","E"],["W","W","W","W","W"]]
a = Solution()
print(a.maxKilledEnemies(grid))				
		
