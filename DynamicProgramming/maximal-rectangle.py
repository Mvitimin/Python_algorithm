import copy
from typing import List

class Solution:
	def maximalRectangle(self, matrix: List[List[str]]) -> int:
		rows = [[int(matrix[i][j]) for j in range(len(matrix[0]))] for i in range(len(matrix))]
		cols = copy.deepcopy(rows)
		if not matrix:
			return 0
		ans = 0
		for i in range(len(matrix)):
			for j in range(1, len(matrix[0])):
				if rows[i][j] == 1:
					rows[i][j] += rows[i][j - 1]
		for j in range(len(matrix[0])):
			for i in range(1, len(matrix)):
				if cols[i][j] == 1:
					cols[i][j] += cols[i - 1][j]
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				if cols[i][j] != 0:
					h, r, prev, matrix[i][j] = 1, i, rows[i][j], rows[i][j]
					while h < cols[i][j]:
						r -= 1
						h += 1
						prev = min(rows[r][j], prev)
						matrix[i][j] = max(matrix[i][j], prev * h)
					ans = max(int(matrix[i][j]), ans)
		
		#print(rows)
		#print(cols)
		#print(matrix)
		return ans
					
a = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]				
'''
matrix = [["0"]]
matrix = [["0","0","1"],["1","1","1"]]
matrix=[["0","0","0","0","0","0","1"],
["0","0","0","0","1","1","1"],
["1","1","1","1","1","1","1"],
["0","0","0","1","1","1","1"]]
'''
print(a.maximalRectangle(matrix))										
					
