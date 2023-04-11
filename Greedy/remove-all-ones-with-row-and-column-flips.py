from typing import List

class Solution:
	def removeOnes(self, grid: List[List[int]]) -> bool:
		
		rows, cols = set(), set()
		m, n = len(grid), len(grid[0])
		table = [[0] * n for _ in range(m)]
		
		for i in range(m):
			if grid[i][0] == 1:
				for j in range(n):
					table[i][j] = 1
		
		for j in range(n):
			if grid[0][j] != table[0][j]:
				for i in range(m):
					table[i][j] ^= 1
			for i in range(m):
				if table[i][j] != grid[i][j]:
					return False
		
								
		return True

		
		
				

a = Solution()
grid = [[0,1,0],[1,0,1],[0,1,0]]
grid = [[1,1,0],[0,0,0],[0,0,0]]
grid = [[0,0,0],[1,1,1]]
#grid = [[1]]
#grid = [[0]]
print(a.removeOnes(grid))		
									
							
