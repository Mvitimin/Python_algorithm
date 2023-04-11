from typing import List

class Solution:
	def numSubmat(self, mat: List[List[int]]) -> int:
		R, C = len(mat), len(mat[0])
		ans = 0
		for r in range(R):
			cnt, stack = 0, []
			for c in range(C):
				if r > 0 and mat[r][c] == 1:
					mat[r][c] += mat[r - 1][c]
				
				while stack and mat[r][c] < m — at[r][stack[-1]]:
					j = stack.pop()
					k = stack[-1] if stack else -1
					cnt -= (j - k) * (mat[r][j] - mat[r][c])
					print("r: {}, r: {}, j: {}, k: {}, cnt: {}".format(r, c, j, k, cnt))
				
				stack.append(c)
				cnt += mat[r][c]
				ans += cnt
				print("r: {}, c: {}, stack: {}, cnt: {}".format(r, c, stack, cnt))
				
		return ans		
						
mat = [[1,0,1],[1,1,0],[1,1,0]]		
a = Solution()
print(a.numSubmat(mat))
