from typing import List

class Solution:
	def exist(self, board: List[List[str]], word: str) -> bool:
		m, n, l = len(board), len(board[0]), len(word)
		
		def solve(i, j, k, visited):
			if k >= l: 
				return True
			for nx, ny in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
				if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == word[k] and (nx, ny) not in visited:
					visited.add((nx, ny))
					if solve(nx, ny, k + 1, visited):
						return True
					visited.remove((nx, ny))
			return False		
		
		for i in range(m):
			for j in range(n):
				if board[i][j] == word[0]:
					visited = set()
					visited.add((i, j))
					if solve(i, j, 1, visited): return True				
		return False
		
		
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]; word = "ABCCED"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]; word = "SEE"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]; word = "ABCB"
a = Solution()
print(a.exist(board, word))
