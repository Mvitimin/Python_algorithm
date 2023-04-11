from typing import List

class Solution:
	def rotate(self, matrix: List[List[int]]) -> None:
		n = len(matrix)
		#(col, n - row - 1)
		for i in range((n + 1) // 2):
			for j in range(n // 2):
				a, b, c, d = matrix[i][j], matrix[j][n - i - 1], matrix[n - i - 1][n - j - 1], matrix[n - j - 1][i] 
				matrix[i][j] = d
				matrix[j][n - i - 1] = a
				matrix[n - i - 1][n - j - 1] = b
				matrix[n - j - 1][i] = c
					
							
		#print(matrix)

a = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(a.rotate(matrix))	
