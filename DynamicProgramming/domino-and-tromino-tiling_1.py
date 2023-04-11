class Solution:
	def numTilings(self, n: int) -> int:
		dp = [0] * (max(n, 2) + 1)
		dp[0] = dp[1] = 1
		dp[2] = 2
		
		M = 10 ** 9 + 7
		for i in range(3, n + 1):
			dp[i] = dp[i - 3] * 2 + dp[i - 1] + dp[i - 2]	
			dp[i - 2] += dp[i - 3]
			dp[i] %= M 
		return dp[n]		

a = Solution()
n = 30
print(a.numTilings(n))	
			
						
		
