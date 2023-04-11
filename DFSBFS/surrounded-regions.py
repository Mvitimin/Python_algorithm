from typing import List
import collections
from itertools import product

class Solution:
	def solve(self, board: List[List[str]]) -> None:
		dx = [1, -1, 0, 0]
		dy = [0, 0, 1, -1]
		n, m = len(board), len(board[0])
		visited = [[0] * m for _ in range(n)]
		def dfs(x, y):
			for i in range(4):
				nx, ny = x + dx[i], y + dy[i]
				if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 'O' and not visited[nx][ny]:
					visited[nx][ny] = 1
					dfs(nx, ny)
			
		borders = list(product(range(n), [0, m - 1])) \
		+ list(product([0, n - 1], range(m)))		
									
		for i, j in borders:
			if board[i][j] == 'O' and not visited[i][j]:
				visited[i][j] = 1
				dfs(i, j)
									
		for i in range(n):
			for j in range(m):
				if not visited[i][j] and board[i][j] == 'O':
					board[i][j] = 'X'
		
a = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
a.solve(board)						
					
						
				
			
						
		

