# path-with-maximum-gold
import copy
from typing import List

class Solution:
	def getMaximumGold(self, grid: List[List[int]]) -> int:
		dx = [0, 0, 1, -1]
		dy = [1, -1, 0, 0]
		N, M = len(grid), len(grid[0])
		visited = [[0] * M for _ in range(N)]		
		ans = 0
		def findPath(sx, sy, t):
			nonlocal ans	
			ans = max(t, ans)
			for i in range(4):
				x, y = sx + dx[i], sy + dy[i]
				if 0 <= x < N and 0 <= y < M:
					if not visited[x][y] and grid[x][y]:
						visited[x][y] = 1
						#print(x, y, grid[x][y], t)
						findPath(x, y, t + grid[x][y]) 
						visited[x][y] = 0
	
		for i in range(N):
			for j in range(M):
				if grid[i][j] != 0:
					visited[i][j] = 1
					findPath(i, j, grid[i][j])		
					visited[i][j] = 0
			
		return ans	
		
		
a = Solution()
#grid = [[0,6,0],[5,8,7],[0,9,0]]
grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
print(a.getMaximumGold(grid))
