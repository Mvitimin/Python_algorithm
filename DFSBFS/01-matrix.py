from typing import List
import collections
class Solution:
	def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
		dx = [1, -1, 0, 0]
		dy = [0, 0, 1, -1]
		n, m = len(mat), len(mat[0])
		distances = [[float('inf')] * m for _ in range(n)]
		q = collections.deque([])
		for i in range(n):
			for j in range(m):
				if mat[i][j] == 0:
					distances[i][j] = 0
					q.append((0, i, j))
			
		while q:
			dist, x, y = q.popleft()
			for i in range(4):
				nx, ny = x + dx[i], y + dy[i]
				if 0 <= nx < n and 0 <= ny < m:
					if mat[nx][ny] == 1:
						if distances[nx][ny] > dist + 1:
							distances[nx][ny] = dist + 1
							q.append((dist + 1, nx, ny))
		
		return distances
		
	
a = Solution()
mat = [[0,1,0],[0,1,0],[1,1,1]]
#mat = [[0,0,0],[0,1,0],[0,0,0]]
print(a.updateMatrix(mat))
			

