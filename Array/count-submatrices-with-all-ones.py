from typing import List

class Solution:
	def numSubmat(self, mat: List[List[int]]) -> int:
		n, m = len(mat), len(mat[0])
		heights = [0] * (m + 1)
		ans = 0
		for i in range(n):
			dp = [0] * (m + 1)
			stack = [-1]
			for j in range(m):
				if mat[i][j]: heights[j] += 1 
				else: heights[j] = 0
				area = 0
				while heights[stack[-1]] > heights[j]:
					index = stack.pop()
				dp[j] = dp[stack[-1]] + (j - stack[-1]) * heights[j]
				stack.append(j)
			ans += sum(dp)
		return ans
		
a = Solution()
mat = [[1,0,1],[1,1,0],[1,1,0]]	
print(a.numSubmat(mat))""
