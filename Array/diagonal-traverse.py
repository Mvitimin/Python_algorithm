from typing import List

class Solution:
	def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
		n, m = len(mat), len(mat[0])
		ans = []
		
		def solve(x, y):
			if not (0 <= x < n and 0 <= y < m):
				return	
			if (x + y) % 2 == 1:
				ans.append(mat[x][y])	
			solve(x + 1, y - 1)
			if (x + y) % 2 == 0:
				ans.append(mat[x][y])  
				
		for j in range(m):
			solve(0, j)
		for i in range(1, n):
			solve(i, m - 1)	
		return ans 

a = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
#mat = [[1,2],[3,4]]
print(a.findDiagonalOrder(mat))
