from typing import List

class Solution:
	def numSubmat(self, mat: List[List[int]]) -> int:
		m, n, ans = len(mat), len(mat[0]), 0
		histogram = [0] * (n + 1)
		for i in range(m):
			stack, dp = [-1], [0] * (n + 1)
			for j in range(n):
				histogram[j] = 0 if mat[i][j] == 0 else histogram[j] + 1
				while histogram[stack[-1]] > histogram[j]:
					stack.pop()
				dp[j] = dp[stack[-1]] + (j - stack[-1]) * histogram[j]
				stack.append(j)	
			ans += sum(dp)
		return ans		
				
						
#mat = [[1,0,1],[1,1,0],[1,1,0]]		
mat = [[0,1,0],[0,1,1],[1,1,1], [1, 1, 1]]		
a = Solution()
print(a.numSubmat(mat))
