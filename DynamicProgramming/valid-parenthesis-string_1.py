
class Solution:
	def checkValidString(self, s: str) -> bool:
		n = len(s)
		dp = [[False] * (n + 1) for i in range(n + 1)]
		dp[n][0] = True

		for i in range(n - 1, -1, -1):
			for j in range(n + 1):
				if s[i] == ')':
					if j == 0: dp[i][j] = False
					else: dp[i][j] = dp[i + 1][j - 1]
				elif s[i] == '(':
					if j == n: dp[i][j] = False
					else: dp[i][j] = dp[i + 1][j + 1]
				else:
					if j == 0: dp[i][j] = any((dp[i + 1][j + 1], dp[i + 1][j]))
					elif j == n: dp[i][j] = any((dp[i + 1][j - 1], dp[i + 1][j]))
					else: dp[i][j] = any((dp[i + 1][j - 1], dp[i + 1][j + 1], dp[i + 1][j]))
		return dp[0][0]

a = Solution()
s = "(*)()((***))"
s = "**"
print(a.checkValidString(s))
