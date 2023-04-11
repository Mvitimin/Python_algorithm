from typing import List
class Solution:
	def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
		n, m = len(grid), len(grid[0])
		visited = [[0] * m for _ in range(n)]
		dx = [1, -1, 0, 0]
		dy = [0, 0, 1, -1]
		ans = set()
		
		def dfs(x, y):
			visited[x][y] = 1
			for i in range(4):
				nx, ny = x + dx[i], y + dy[i]
				if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == grid[row][col]:
					if not visited[nx][ny]:
						dfs(nx, ny)
				else:
					ans.add((x, y))		
		dfs(row, col)
		for x, y in ans:
			grid[x][y] = color	
		return grid 
					
grid = [[1,1],[1,2]]; row = 0; col = 0; color = 3
#grid = [[1,2,2],[2,3,2]]; row = 0; col = 1; color = 3
#grid = [[1,1,1],[1,1,1],[1,1,1]]; row = 1; col = 1; color = 2
#grid = [[1,1,1,2,2],[2,1,2,2,2],[1,1,2,2,1]]; row = 1; col = 0; color = 1
a = Solution()
print(a.colorBorder(grid, row, col, color))								
					
				
			
			
