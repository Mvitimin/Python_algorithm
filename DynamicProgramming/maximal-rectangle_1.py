from typing import List

class Solution:
	def maximalRectangle(self, matrix: List[List[str]]) -> int:
		if not matrix:
			return 0
		dp = [[int(matrix[i][j]) for j in range(len(matrix[0]))] for i in range(len(matrix))]
		for i in range(len(matrix)):
			for j in range(1, len(matrix[0])):
				if dp[i][j] == 1:
					dp[i][j] += dp[i][j - 1]
		
		def findLargest(col):
			stack, max_area, n = [], 0, len(dp)
			for i in range(n):
				w, h = i, dp[i][col] 
				while stack and stack[-1][-1] > h:
					max_area, w = max(max_area, (i - stack[-1][0]) * stack[-1][-1]), stack[-1][0]					
					stack.pop()
				stack.append((w, h))
			
			while stack:
				max_area = max(max_area, (n - stack[-1][0]) * stack[-1][-1])
				stack.pop()
			return max_area
		
		ans = 0
		for i in range(len(dp[0])):
			ans = max(ans, findLargest(i))
		return ans					

a = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(a.maximalRectangle(matrix))
