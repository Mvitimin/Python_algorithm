from typing import List

class Solution:
	def rotate(self, matrix: List[List[int]]) -> None:
		# col -> row
		# row -> (n - 1 - i) col 
		# (j, (n - 1 - i))
		n = len(matrix)
		for i in range(n // 2):
			for j in range(i, n - i - 1):
				prev = matrix[i][j]
				x, y = i, j
				for _ in range(4):
					x, y = y, n - 1 - x
					tmp = matrix[x][y]
					matrix[x][y] = prev 
					prev = tmp
		return matrix
	
a = Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
#matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(a.rotate(matrix))

					
				
				
				
		
