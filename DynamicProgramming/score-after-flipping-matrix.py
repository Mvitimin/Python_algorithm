from typing import List

class Solution:
	def matrixScore(self, grid: List[List[int]]) -> int: 
		n, m = len(grid), len(grid[0])
		for i in range(n):
			if grid[i][0] == 0:
				for j in range(m):
					grid[i][j] ^= 1
		for j in range(m):
			if sum(grid[i][j] == 0 for i in range(n)) > n // 2:
				for i in range(n):
					grid[i][j] ^= 1
		return sum(int(''.join(map(str, grid[i])), 2) for i in range(n))
						
						
					
					
				
			
				
a = Solution()
grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
ans = a.matrixScore(grid)	
print(ans)			
				
				
