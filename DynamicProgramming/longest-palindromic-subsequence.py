class Solution:
	def longestPalindromeSubseq(self, s: str) -> int:
		n = len(s)
		dp = [[0] * n for _ in range(n)]
		dp[n - 1][n - 1] = 1
		for i in range(n - 2, -1, -1):
			for j in range(i, n):
				if j == 0: dp[i][j] = 1
				elif s[i] == s[j]:
					dp[i][j] = max(dp[i][j - 1], dp[i + 1][j - 1] + (1 if i == j else 2))
				else:
					dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
		return dp[0][n - 1]			
		
a = Solution()
s = "bbbab"
s = "cbbd"
s = "caac"
s = "caaaabbbbc"
print(a.longestPalindromeSubseq(s))	
