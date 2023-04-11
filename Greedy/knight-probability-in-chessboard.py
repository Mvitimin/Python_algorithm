from functools import lru_cache

class Solution:
	def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
		dx = [1, 1, 2, 2, -1, -1, -2, -2]
		dy = [-2, 2, -1, 1, -2, 2, -1, 1]
		m = len(dx)
		@lru_cache(None)
		def dfs(x, y, t):
			if t == k:
				return 1
			cnt = 0	
			for i in range(m):
				nx, ny = x + dx[i], y + dy[i]
				if 0 <= nx < n and 0 <= ny < n:
					cnt += dfs(nx, ny, t + 1)
			return cnt					
		return dfs(row, column, 0) / (m ** k)


a = Solution()
n = 3; k = 2; row = 0; column = 0
n = 1; k = 0; row = 0; column = 0
print(a.knightProbability(n, k, row, column))
