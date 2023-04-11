from typing import List
class Solution:
	def findBall(self, grid: List[List[int]]) -> List[int]:
		m, n = len(grid), len(grid[0])
		dp = [[(1 if i == 0 else 0) for j in range(n)] for i in range(m + 1)]
		ans = [-1] * n
		for j in range(n):
			start = j
			for i in range(m):
				direction = grid[i][start]
				start += grid[i][start]
				if start >= n or start < 0 or grid[i][start] != direction:
					break
			else:
				ans[j] = start
		return ans
			
				

a = Solution()
#grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
#grid = [[-1]]
print(a.findBall(grid))			
						
					
				

