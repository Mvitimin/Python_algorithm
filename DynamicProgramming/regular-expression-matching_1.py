from functools import lru_cache

class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		m, n = len(s), len(p)
		
		dp = [[False] * (n + 1) for _ in range(m + 1)] 
		
		dp[-1][-1] = True
				
		for i in range(-1, m):
			for j in range(n):
				if s[i] == p[j] or p[j] == '.':
					dp[i][j] = dp[i - 1][j - 1] or (j + 1 < n and p[j + 1] == '*' and dp[i - 1][j]) 
				if p[j] == '*':
					dp[i][j] = dp[i][j] or dp[i][j - 2] or dp[i][j - 1] 
		return dp[m - 1][n - 1]
			
a = Solution()
s = "aa"; p = "a"
#s = "aa"; p = "a*"
s = "aab"; p = "c*a*b"
#s = "abcd"; p = "d*"
#s = "ab"; p = ".*"
#s = "mississippi"; p = "mis*is*p*."
#s = "a"; p = "ab*"
#s = "aabcbcbcaccbcaabc"; p = ".*a*aa*.*b*.c*.*a*"
#s = "aaa"; p = "ab*a"
#s = "aaabaaaababcbccbaab"; p = "c*c*.*c*a*..*c*"
print(a.isMatch(s, p))				
