from typing import List
class NumMatrix:
	def __init__(self, matrix: List[List[int]]):
		m, n = len(matrix), len(matrix[0])
		self.dp = [[0] * (n + 1) for _ in range(m + 1)]
		for i in range(n):
			for j in range(m):
				self.dp[i][j] = self.dp[i - 1][j] + self.dp[i][j - 1] - self.dp[i - 1][j - 1] + matrix[i][j]
		
		
	def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
		return self.dp[row2][col2] - self.dp[row1 - 1][col2] - self.dp[row2][col1 - 1] + self.dp[row1 - 1][col1 - 1]
		
						
		
numMatrix = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);						
t = numMatrix.sumRegion(2, 1, 4, 3);
print(t)
t = numMatrix.sumRegion(1, 1, 2, 2);
print(t)
t = numMatrix.sumRegion(1, 2, 2, 4);
print(t)
			
		
		

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


