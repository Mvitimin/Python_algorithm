class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		
		m, n = len(p), len(s)
		dp = [[False] * (n + 1) for _ in range(m + 1)]
		dp[0][0] = True
		for i in range(1, m + 1):
			if p[i - 1] == '*':
				dp[i][0] = dp[i - 1][0]
		
		for i in range(1, m + 1):
			for j in range(1, n + 1):
				if p[i - 1] == '*':
					dp[i][j] = (dp[i - 1][j - 1] or dp[i][j - 1] or dp[i - 1][j])
				else:
					dp[i][j] = dp[i - 1][j - 1] and p[i - 1] in [s[j - 1], '?']
			
		return dp[-1][-1]			
					
a = Solution()
s = "aa"; p = "*"
s = "cb"; p = "?a"
s ="abcabczzzde";p ="*abc???de*"
print(a.isMatch(s, p))			
		
