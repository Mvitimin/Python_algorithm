from typing import List
import copy
class Solution:
	def solveSudoku(self, board: List[List[str]]) -> None:
		n, m = 9, 3
		rows = [set([str(i) for i in range(1, n + 1)]) for _ in range(n)]
		cols = [set([str(i) for i in range(1, n + 1)]) for _ in range(n)]
		groups = [[set([str(i) for i in range(1, n + 1)]) for _ in range(m)] for _ in range(m)]
		
		event = []
		for i in range(n):
			for j in range(n):
				if board[i][j] != '.':
					rows[i].remove(board[i][j])
					cols[j].remove(board[i][j])
					groups[i // m][j // m].remove(board[i][j])
				else: 
					event.append((i, j))
		
		
		def solve(k):	
			if k >= len(event):
				return True
			i, j = event[k]
			intersection = rows[i] & cols[j] & groups[i // m][j // m]
			if not intersection: return False
			for p in intersection:	
				rows[i].remove(p)
				cols[j].remove(p)
				groups[i // m][j // m].remove(p)
				board[i][j] = p
				if solve(k + 1): return True
				rows[i].add(p)
				cols[j].add(p)
				groups[i // m][j // m].add(p)
				board[i][j] = '.'												
			return False
		solve(0)
		
		
		
a = Solution()
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
print(a.solveSudoku(board))


