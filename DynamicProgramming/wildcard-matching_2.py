from functools import lru_cache
class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		n, m = len(s), len(p)
		dp = [[0] * (n + 1) for _ in range(m + 1)]
		dp[m][n] = 1
		for i in range(m - 1, -1, -1):
			for j in range(n, -1 , -1):
				if j <= n - 1 and p[i] in ['*', '?', s[j]]:
					dp[i][j] = dp[i + 1][j + 1]
				if p[i] == '*':
					if j <= n - 1:
						dp[i][j] = max(dp[i][j], dp[i][j + 1])
					dp[i][j] = max(dp[i][j], dp[i + 1][j])
		return dp[0][0] == 1
		
s = "cb"; p = "?a"
s = "adceb"; p = "*a*b"
s = "acdcb"; p = "a*c?b"
#s = ""; p = "******"
s = "abcabczzzde"; p = "*abc???de*"
a = Solution()
print(a.isMatch(s, p))
