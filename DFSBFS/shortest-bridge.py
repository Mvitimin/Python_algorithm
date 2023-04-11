from typing import List
import collections

class Solution:
	def shortestBridge(self, grid: List[List[int]]) -> int:
		n, m = len(grid), len(grid[0])
		dx = [0, 0, 1, -1]
		dy = [1, -1, 0, 0]
		visited = [[0] * m for _ in range(n)]
		q = collections.deque([])
		def dfs(x, y):
			for i in range(4):
				nx = x + dx[i]
				ny = y + dy[i]
				if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] != 1 and grid[nx][ny]:
					visited[nx][ny] = 1
					q.append((0, nx, ny))
					dfs(nx, ny)
		
		for i in range(n):
			for j in range(m):
				if not q and grid[i][j] and visited[i][j] != 1:
					q.append((0, i, j))
					visited[i][j] = 1
					dfs(i, j)
					break
		
		while q:
			cost, x, y = q.popleft()
			if cost > 0 and grid[x][y] == 1:
				return cost - 1
			for i in range(4):
				nx = x + dx[i]
				ny = y + dy[i]
				if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] != 1:
					visited[nx][ny] = 1
					q.append((cost + 1, nx, ny))
		return 1 
		
		
							 
		
a = Solution()
grid = [[0,1],[1,0]]
#grid = [[0,1,0],[0,0,0],[0,0,1]]
#grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
print(a.shortestBridge(grid))
