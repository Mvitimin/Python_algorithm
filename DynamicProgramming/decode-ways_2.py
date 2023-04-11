
from functools import lru_cache

class Solution:
	def numDecodings(self, s: str) -> int:
		
		n = len(s)
		maps = set()
		for i in range(26):
			maps.add(str(i + 1))
		
		dp = [0] * (n + 2)
		dp[-1] = 1
			
		for i in range(n):
			if s[i:i + 1] in maps:
				dp[i] += dp[i - 1]
			if s[max(i - 1, 0):i + 1] in maps:
				dp[i]	+= dp[i - 2]
		return dp[n - 1]
		
a = Solution()
s = ""
s = "06"
s = "226"
print(a.numDecodings(s))
