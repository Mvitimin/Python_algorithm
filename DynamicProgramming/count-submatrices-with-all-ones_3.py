from typing import List

class Solution:
	def numSubmat(self, mat: List[List[int]]) -> int:
		m, n = len(mat), len(mat[0])
		hist = [0] * n
		ans = 0
		for i in range(m):
			stack = []
			for j in range(n):
				hist[j] = hist[j] + 1 if mat[i][j] else 0
				start = j
				while stack and stack[-1][1] > hist[j]:
					start = stack[-1][0]
					stack.pop()
				stack.append((start, hist[j]))
				end = j	+ 1
				for index, h in reversed(stack):
					ans += h * (end - index)
					end = index							
		return ans
		
a = Solution()
mat = [[1,0,1],[1,1,0],[1,1,0]]
print(a.numSubmat(mat))				
					

