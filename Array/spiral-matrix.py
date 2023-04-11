
from typing import List

class Solution:
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		n, m = len(matrix), len(matrix[0])
		VISITED = -101
		dx = [0, 1, 0, -1]
		dy = [1, 0, -1, 0]
		ans = []
		
		def isOutBound(x, y):
			return not (0 <= x < n and 0 <= y < m) or matrix[x][y] == VISITED
		
		def solve(x, y, direction):
			if isOutBound(x, y):
				return 
			ans.append(matrix[x][y])
			matrix[x][y] = VISITED
			if isOutBound(x + dx[direction], y + dy[direction]):
				direction = (direction + 1) % 4
			solve(x + dx[direction], y + dy[direction], direction)
		
		solve(0, 0, 0)
		return ans
		
a = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(a.spiralOrder(matrix))
