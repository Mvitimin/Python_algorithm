from typing import List

class Solution:
	def numSubmat(self, mat: List[List[int]]) -> int:
		r, c, ans = len(mat), len(mat[0]), 0
		histogram = [0] * (c + 1)
		for i in range(r):
			stack, dp = [-1], [0] * (c + 1)
			for j in range(c):
				histogram[j] = histogram[j] + 1 if mat[i][j] == 1 else 0
				while stack and histogram[stack[-1]] > histogram[j]:
					stack.pop()
				dp[j] = dp[stack[-1]] + (j - stack[-1]) * histogram[j]
				stack.append(j)
			ans += sum(dp)
				
		return ans


a = Solution()
#mat = [[1,0,1],[1,1,0],[1,1,0]]
mat = [[1,0,1],[0,1,0],[1,0,1]]
print(a.numSubmat(mat))
