
class Solution:
	def countSubstrings(self, s: str) -> int:
		n = len(s)
		dp = [[0] * n for _ in range(n)]
		ans = 0
		for j in range(n):
			for i in range(j + 1):
				if i == j: dp[i][j] = 1
				else:
					if s[i] == s[j]:
						dp[i][j] += 1 if i + 1 >= j - 1 else dp[i + 1][j - 1]		
				ans += dp[i][j]
		return ans
		
a = Solution()
s = "abc"
s = "abba"

print(a.countSubstrings(s))
