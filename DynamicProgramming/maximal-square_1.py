from typing import List

class Solution:
	def maximalSquare(self, matrix: List[List[str]]) -> int:
		m, n = len(matrix), len(matrix[0])
		dp = [[0] * (n + 1) for _ in range(m + 1)]
		
		ans = 0
		for i in range(m):
			for j in range(n):
				if matrix[i][j] != "1": continue
				dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
				ans = max(ans, dp[i][j])
		return ans ** 2
		
a = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
#matrix = [["0","1"],["1","0"]]
print(a.maximalSquare(matrix))
				
				
				

