class Solution:
	def palindromePartition(self, s: str, k: int) -> int:
		n = len(s)
		dp = [[n] * n for _ in range(n)]
		dp2 = [[n] * n for _ in range(k)]
		
		for i in range(n):
			dp[i][i] = 0
			if i + 1 < n:
				dp[i + 1][i] = 0
		
		for l in range(2, n + 1):
			for i in range(n):
				j = i + l - 1
				if j < n:
					dp[i][j] = min(dp[i][j], dp[i + 1][j - 1] + (1 if s[i] != s[j] else 0))
		
		for i in range(n):
			dp2[0][i] = dp[0][i]
			
		
		for l in range(1, k):
			for j in range(1, n):
				for i in range(1, j + 1):
					dp2[l][j] = min(dp2[l][j], dp2[l - 1][i - 1] + dp[i][j])
		return dp2[k - 1][n - 1]			
				
a = Solution()
s = "abc"; k = 2 
s = "aea"; k = 2
#s = "aabbc"; k = 3
#s = "leetcode"; k = 8
#s = "oiwwhqjkb"; k = 1
print(a.palindromePartition(s, k))
		
