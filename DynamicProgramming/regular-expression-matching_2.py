class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		
		m, n = len(s), len(p)

		dp = [[False] * (m + 1) for _ in range(n + 1)]
		
		dp[0][0] = True
		
		for i, pc in enumerate(p, 1):
			dp[i][0] = (pc == '*' and dp[i - 2][0])
			
		for i, pc in enumerate(p, 1):
			for j, sc in enumerate(s, 1):
				if pc != '*':
					dp[i][j] = dp[i - 1][j - 1] and (pc in [sc, '.'])	
				else:
					dp[i][j] = dp[i - 2][j] or (dp[i][j - 1] and p[i - 2] in [sc, '.'])
		
		'''
		for i in range(n + 1):
			print(p[i - 1] if i > 0 else '', dp[i])
			print()
		'''
		return dp[-1][-1]
		
		
a = Solution()
s = "abbc"; p = "ab*."
#s = "aa"; p = "a"
#s = "aa"; p = "a*"
#s = "ab"; p = ".*"
#s = "aabkc"; p = "aa.*c"
#s = "aaa"; p = "ab*ac*a"
#s = "aaa"; p = "ab*a*c*a"
print(a.isMatch(s, p))		
			
			
		
