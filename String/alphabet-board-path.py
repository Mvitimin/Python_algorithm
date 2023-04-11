import collections
from typing import List

class Solution:
	def alphabetBoardPath(self, target: str) -> str:
		board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
		moves = {
			'U': (-1, 0),
			'D': (1, 0),
			'L': (0, -1),
			'R': (0, 1)
		}
		def bfs(curs: List, index: int):
			q = collections.deque([(curs[0], curs[1], '')])
			visited = [[0 for j in range(len(board[i]))] for i in range(len(board))]
			while q:
				r, c, path = q.popleft()
				if board[r][c] == target[index]:
					return (r, c, '{}!'.format(path))				
				
				for m in moves:
					dr = r + moves[m][0]
					dc = c + moves[m][1]
					if 0 <= dr < len(board) and 0 <= dc < len(board[dr]):
						if not visited[dr][dc]:
							q.append((dr, dc, '{}{}'.format(path, m)))
							visited[dr][dc] = 1
			return None
		

		r, c, ans = 0, 0, []
		for i in range(len(target)):
			res = bfs([r, c], i)
			if res is None:
				return ''
			r, c = res[0], res[1]
			ans.append(res[2])
		return ''.join(ans)	
				

a = Solution()
#target = "leet"
target = "code"
print(a.alphabetBoardPath(target))
				
				
		
		
