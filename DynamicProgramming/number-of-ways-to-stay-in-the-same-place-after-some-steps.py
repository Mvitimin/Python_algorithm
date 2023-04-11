from functools import lru_cache
class Solution:
	def numWays(self, steps: int, arrLen: int) -> int:
		
		MODULO = 10 ** 9 + 7
		maxRight = min(steps // 2 + 1, arrLen)
		dp = [[0] * (maxRight + 2) for i in range(steps + 1)]
		
		dp[1][0] = 1
		
		for i in range(1, steps + 1):
			for j in range(maxRight):
				dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1] + dp[i - 1][j + 1]) % MODULO
		
		return (dp[steps][0] + dp[steps][1]) % MODULO
	
		

a = Solution()
steps = 3; arrLen = 2
steps = 2; arrLen = 4
#steps = 4; arrLen = 2
#steps = 3; arrLen = 3
#steps = 430; arrLen = 148488
print(a.numWays(steps, arrLen))


