import collections

class Solution:
	def numDistinct(self, s: str, t: str) -> int:
		n, m = len(s), len(t)
		dp = [[0] * (m + 1) for _ in range(n + 1)]
		for i in range(n + 1):
			dp[i][0] = 1
		
		for i in range(1, n + 1):
			for j in range(1, m + 1):
				dp[i][j] = dp[i - 1][j]				
				if s[i - 1] == t[j - 1]:
					dp[i][j] += dp[i - 1][j - 1]
		print(dp)
		return dp[-1][-1]
				
				
				

a = Solution()
s = "rabbbit"; t = "rabbit"
s = "babgbag"; t = "bag"
print(a.numDistinct(s, t))

				
				
	
