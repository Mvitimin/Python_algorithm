class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		m, n = len(s), len(p)
		dp = [[False] * (n + 1) for _ in range(m + 1)]
		
		dp[-1][-1] = True
		
		for i in range(n):
			if p[i] == '*':
				dp[-1][i] = dp[-1][i - 1]
			else:
				dp[-1][i] = False
			
		
		for i in range(m):
			for j in range(n):
				if p[j] == '*':
					dp[i][j] = dp[i - 1][j] or dp[i - 1][j - 1] or dp[i][j - 1]
				elif p[j] == '?':
					dp[i][j] = dp[i - 1][j - 1]
				else:
					dp[i][j] = dp[i - 1][j - 1] and p[j] == s[i]
		
		'''
		for i in range(m):
			print(dp[i])
		'''
		return dp[m - 1][n - 1]

a = Solution()
s = "aa"; p = "a"
s = "aa"; p = "*"
s = "cb"; p = "?a"
s = "adceb"; p = "*a*b"
print(a.isMatch(s, p))			
					
			
		
