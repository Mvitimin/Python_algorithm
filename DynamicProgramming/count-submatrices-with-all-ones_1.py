from typing import List

class Solution:
	def numSubmat(self, mat: List[List[int]]) -> int:
		n, m = len(mat), len(mat[0])
		dp = [[0 for i in range(m)] for j in range(n)]
		for i in range(n):
			stack, histo = [-1], [0] * n
			for j in range(m):
				if mat[i][j] == 0:
					continue
				histo[j] = histo[j - 1] + 1 if j > 1 else 1
				while stack and histo[stack[-1]] > histo[j]:
					stack.pop()
				dp[i][j] = dp[i][stack[-1]] + 
				
				

