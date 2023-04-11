from typing	import List

class Solution:
	def rotate(self, matrix: List[List[int]]) -> None:
		n = len(matrix)
		
		def swap(row, col):
			a, b = matrix[row][col], matrix[col][n - row - 1]
			c, d = matrix[n - row - 1][n - col - 1], matrix[n - col - 1][row]
			
			matrix[row][col], matrix[col][n - row - 1] = d, a
			matrix[n - row - 1][n - col - 1], matrix[n - col - 1][row] = b, c
			
		for i in range(n, 1, -1):
			row = col = n - i
			for j in range(n - i, i - 1):
				col = j
				swap(row, col)
		#print(matrix)
				
a = Solution()
#matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(a.rotate(matrix))				
				
			
			
