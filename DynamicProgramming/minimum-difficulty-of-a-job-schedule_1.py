from typing import List

class Solution:
	def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
		n = len(jobDifficulty)
		dp = [[float('inf')] * n for _ in range(d)]
		dp[0][0] = jobDifficulty[0]
		for i in range(1, n):
			dp[0][i] = max(jobDifficulty[i], dp[0][i - 1])
		
		for i in range(1, d):
			for j in range(i, n):
				max_diff = 0
				for k in range(j, i - 1, -1):
					max_diff = max(jobDifficulty[k], max_diff)
					dp[i][j] = min(dp[i][j], dp[i - 1][k - 1] + max_diff)
		return dp[-1][-1]	if dp[-1][-1] != float('inf') else -1		
			
				
				
				
						
				
				
				
			
					
a = Solution()
#jobDifficulty = [6,5,4,3,2,1]; d = 2
#jobDifficulty = [9,9,9]; d = 4
#jobDifficulty = [1,1,1]; d = 3
#jobDifficulty = [7,1,7,1,7,1]; d = 3
jobDifficulty = [11,111,22,222,33,333,44,444]; d = 6
print(a.minDifficulty(jobDifficulty, d))				
			
		
