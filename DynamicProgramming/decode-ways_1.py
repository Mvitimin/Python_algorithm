
class Solution:
	def numDecodings(self, s: str) -> int:
		n = len(s)
		dp = [0] * (n + 1)
		dp[n] = 1
		for i in range(len(s) - 1, -1, -1):
			if s[i] != '0':
				dp[i] += dp[i + 1]
				dp[i] += dp[i + 2] if i + 2 <= n and int(s[i:i + 2]) <= 26 else 0
		return dp[0]
					
a = Solution()
s = "12"
s = "11106"
s = "226"
#s = "0"
print(a.numDecodings(s))
