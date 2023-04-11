from typing import List

class Solution:
	def minPathSum(self, grid: List[List[int]]) -> int:
		m, n = len(grid), len(grid[0])
		
		for i in range(m):
			for j in range(n):
				if i == 0 and j == 0: continue
				up, left = float('inf') if i < 1 else grid[i - 1][j], float('inf') if j < 1 else grid[i][j - 1]
				grid[i][j] = min(up, left) + grid[i][j]
		return grid[-1][-1]

a = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
grid = [[1,2,3],[4,5,6]]
print(a.minPathSum(grid))
			
