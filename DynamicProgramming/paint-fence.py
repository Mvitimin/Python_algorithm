class Solution:
	def numWays(self, n: int, k: int) -> int:
		dp = [0] * (n + 2)
		dp[-1] = 1
					
		for i in range(n):
			s = (dp[i - 2] + dp[i - 1]) 
			dp[i] = s * (k - 1)	
		print(dp)
		return s * k

a = Solution()
n = 3; k = 2
#n = 7; k = 2
#n = 7; k = 2
#n = 1; k = 1
print(a.numWays(n, k))
