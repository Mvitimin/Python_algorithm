class Solution:
	def numTilings(self, n: int) -> int:
		dp = [0] * (n + 1 if n >= 3 else 3)
		dp2 = [0] * (n + 1 if n >= 3 else 3)
		dp[0] = dp[1] = dp2[0] = 1
		dp2[1] = dp[2] = 2
		dp2[2] = 4
			
		for i in range(3, n + 1):
			dp[i] = dp[i - 1] + dp[i - 2] + dp2[i - 3] * 2
			dp2[i] = dp2[i - 1] + dp[i]
				
		return dp[n] % (10 ** 9 + 7)
		
a = Solution()
n = 3
n = 4
n = 5
print(a.numTilings(n))
							
			
		
		
