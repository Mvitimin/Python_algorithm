from typing import List
class Solution:
	def minDifficulty(self, A: List[int], d: int) -> int:
		n = len(A)
		if n < d: return -1
		dp, dp2 = [float('inf')] * n, [0] * n
		for i in range(d):
			stack = []
			for j in range(i, n):
				dp2[j] = dp[j - 1] + A[j] if j else A[j]
			
				while stack and A[stack[-1]] <= A[j]:
					k = stack.pop()
					dp2[j] = min(dp2[j], dp2[k] - A[k] + A[j])
		
				if stack:
					dp2[j] = min(dp2[j], dp2[stack[-1]])
				stack.append(j)
			dp, dp2 = dp2, dp					
		return dp[-1]


a = Solution()
jobDifficulty = [4, 6, 7, 1, 3]; d = 2
print(a.minDifficulty(jobDifficulty, d))
