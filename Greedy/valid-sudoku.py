from typing import List

class Solution:
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		N, M = 9, 3 
		groups = [[set([str(i) for i in range(1, N + 1)]) for _ in range(M)] for _ in range(M)]
		rows = [set([str(i) for i in range(1, N + 1)]) for _ in range(N)]		
		cols = [set([str(i) for i in range(1, N + 1)]) for _ in range(N)]
		empty = []
				
		for i in range(N):
			for j in range(N):
				if board[i][j] != '.':
					if board[i][j] in groups[i // 3][j // 3]:
						groups[i // 3][j // 3].remove(board[i][j])
					else:
						return False
				
					if board[i][j] in rows[i]:
						rows[i].remove(board[i][j])
					else:
						return False	
				else: 
					empty.append((i, j))
		
		for j in range(N):
			for i in range(N):
				if board[i][j] != '.':
					if board[i][j] in cols[j]:
						cols[j].remove(board[i][j])
					else: 
						return False			
								
		def check(index):
			if index >= len(empty):
				return True
			row, col = empty[index]
			if board[row][col] == '.':
				possibles = (rows[row] & cols[col] & groups[row // 3][col // 3])
				if not possibles:
					print(row, col, rows[row], cols[col], groups[row // 3][col // 3]'')
					return False
				for p in possibles:
					board[row][col] = p 
					rows[row].remove(p)
					cols[col].remove(p)
					groups[row // 3][col // 3].remove(p)
					if check(index + 1):
						return True
					board[row][col] = '.' 
					rows[row].add(p)
					cols[col].add(p)
					groups[row // 3][col // 3].add(p)	
			return False
		return check(0)
			

a = Solution()
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]

'''
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
'''
print(a.isValidSudoku(board))


