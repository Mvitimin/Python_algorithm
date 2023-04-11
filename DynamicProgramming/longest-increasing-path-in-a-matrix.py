from typing import List

class Solution:
	def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
		m, n = len(matrix), len(matrix[0])
		event = []
		for i in range(m):
			for j in range(n):
				event.append((matrix[i][j], i, j))
		event.sort(reverse=True)
		
		dp = [[0] * n for _ in range(m)]
		
		def find(r, c):	
			val = 1
			for i, j in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
				if 0 <= i < m and 0 <= j < n and matrix[i][j] > matrix[r][c]:
					val = max(1 + dp[i][j], val)
			return val 
		
		ans = 0
		for v, r, c in event:
			dp[r][c] = find(r, c)
			ans = max(ans, dp[r][c])
		
		return ans
				
					
a = Solution()
matrix = [[9,9,4],[6,6,8],[2,1,1]]
matrix = [[3,4,5],[3,2,6],[2,2,1]]
matrix = [[1]]
print(a.longestIncreasingPath(matrix))				
