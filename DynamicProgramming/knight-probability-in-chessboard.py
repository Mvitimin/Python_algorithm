
class Solution:
	def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
		dx = [1, 1, 2, 2, -1, -1, -2, -2]
		dy = [-2, 2, -1, 1, -2, 2, -1, 1]
		m = len(dx)
		dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
		if k == 0:
			dp[k][row][column] = 1
		for t in range(k):
			for i in range(n):
				for j in range(n):
					if t == 0: dp[t][i][j] = 1
					for p in range(m):
						nx, ny = i + dx[p], j + dy[p]
						if 0 <= nx < n and 0 <= ny < n:
							dp[t + 1][nx][ny] += (dp[t][i][j])
														
		return dp[k][row][column] / m ** k 

a = Solution()
n = 3; k = 2; row = 0; column = 0
#n = 3; k = 1; row = 0; column = 0
#n = 3; k = 3; row = 0; column = 0
#n = 1; k = 0; row = 0; column = 0
print(a.knightProbability(n, k, row, column)) 
			
			

