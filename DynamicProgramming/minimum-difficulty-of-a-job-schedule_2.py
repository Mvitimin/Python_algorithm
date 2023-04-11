from typing import List
class Solution:
	def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
		n = len(jobDifficulty)
		table = [[0] * (n) for _ in range(n)]
		dp = [[float('inf')] * (n + 1) for _ in range(d + 1)]
		dp[-1][-1] = 0
	
		for i in range(n):
			maxJob = jobDifficulty[i]
			for j in range(i, n):
				maxJob = max(maxJob, jobDifficulty[j])
				table[i][j] = maxJob
		
		for k in range(d):
			for j in range(k, n):
				for i in range(k, j + 1):
					dp[k][j] = min(dp[k][j], dp[k - 1][i - 1] + table[i][j])

					
		return -1 if dp[d - 1][n - 1] == float('inf') else dp[d - 1][n - 1]
					
				
		
	
a = Solution()
jobDifficulty = [6,5,4,3,2,1]; d = 2
#jobDifficulty = [9,9,9]; d = 4
#jobDifficulty = [1,1,1]; d = 3
print(a.minDifficulty(jobDifficulty, d))
		

