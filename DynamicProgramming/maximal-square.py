from typing import List

class Solution:
	def maximalSquare(self, matrix: List[List[str]]) -> int:
		m, n = len(matrix), len(matrix[0])
		widths = [[0] * (n + 1) for i in range(m)]
		ans = 0
		for i in range(m):
			for j in range(1, n + 1):
				if matrix[i][j - 1] == "1":
					widths[i][j] = widths[i][j - 1] + 1 			
				width, l = widths[i][j], 1
				for k in range(i, -1, -1):
					if matrix[k][j - 1] == "1":
						width = min(width, widths[k][j])
						ans = max(ans, min(l, width) ** 2)
						l += 1
					else:
						break				
		return ans

a = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#matrix = [["0","1"],["1","0"]]
#matrix = [["0"]]
'''
matrix = [["1","1","1","1","1","1","1","1"],
          ["1","1","1","1","1","1","1","0"],
          ["1","1","1","1","1","1","1","0"],
          ["1","1","1","1","1","0","0","0"],
          ["0","1","1","1","1","0","0","0"]]
          '''
print(a.maximalSquare(matrix))		
		

