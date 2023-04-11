from typing import List

class Solution:
	def generateMatrix(self, n: int) -> List[List[int]]:
		
		directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
		ans = [[0] * n for _ in range(n)]
		
		cur = 1
		r, c = 0, -1
		d = 0
			
		while cur <= n * n:
			nr, nc = r + directions[d][0], c + directions[d][1] 
			if not (0 <= nr < n and 0 <= nc < n) or ans[nr][nc] > 0:
				d = (d + 1) % 4
				continue
			else:
				ans[nr][nc] = cur 
				r, c = nr, nc 
				cur += 1
		return ans

a = Solution()
n = 1
print(a.generateMatrix(n))		
				
		
			
			
			
			
		
		
		
