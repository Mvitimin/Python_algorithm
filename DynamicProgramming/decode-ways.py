import collections
class Solution:
	def numDecodings(self, s: str) -> int:
		dp = collections.defaultdict(int)
		def findDecodeWays(start):
			if start > len(s):
				return 0
			if start == len(s):
				return 1
			if s[start] == '0':
				return 0
			if start in dp:
				return dp[start]
			dp[start] = findDecodeWays(start + 1) + (findDecodeWays(start + 2) if int(s[start:start + 2]) <= 26 else 0)
			return dp[start]		
		findDecodeWays(0)
		return dp[0]
					
a = Solution()
s = "12"
s = "11106"
#s = "0"
print(a.numDecodings(s))
