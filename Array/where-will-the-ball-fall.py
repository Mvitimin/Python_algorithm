from typing import List

class Solution:
	def findBall(self, grid: List[List[int]]) -> List[int]:
		
		m, n = len(grid), len(grid[0])
		
		
		def fall(column):
			for i in range(m):
				k = grid[i][column]
				column += grid[i][column]
				if column < 0 or column >= n or k != grid[i][column]:
					return -1
			return column
		
		ans = []
		for i in range(n):
			ans.append(fall(i))
		return ans


a = Solution()
grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
#grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
#grid = [[-1]]
print(a.findBall(grid))

			
