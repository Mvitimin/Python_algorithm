class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		m, n = len(s), len(p)
		dp = [[False for j in range(n + 1)] for i in range(m + 1)]
		dp[m][n] = True # s == '' and p == '' 
		for j in range(n):
			if p[j] == '*': 
				dp[m][j] = dp[m][j - 2] 
				
		for i in range(m):
			for j in range(n):
				if p[j] == '*':
					match = p[j - 1] == '.' or p[j - 1] == s[i] 
					dp[i][j] = dp[i][j - 2] or (match and dp[i - 1][j])		
				elif p[j] == '.':
					dp[i][j] = dp[i - 1][j - 1]
				else:
					dp[i][j] = dp[i - 1][j - 1] and s[i] == p[j]
						
		return dp[m - 1][n - 1]
		
a = Solution()
s = "ab"; p = ".*"
s = "aa"; p = "a"
s = "aab"; p = "c*a*b"
s = "mississippi"; p = "mis*is*p*."
#s = "aaa"; p = "ab*ac*a"
print(a.isMatch(s, p))	
#arr = [[0 if i == 1 and j == 2 else 1 for i in range(2)] for j in range(3)]
		
