class Solution:
	def minDistance(self, word1: str, word2: str) -> int:
		m, n = len(word2), len(word1)
		dp = [[float('inf') for j in range(n + 1)] for i in range(m + 1)]
		for j in range(n):
			dp[m][j] = j + 1
		for i in range(m):
			dp[i][n] = i + 1 
		dp[-1][-1] = 0
				
		for i in range(m):
			for j in range(n):
				dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)
				if word2[i] == word1[j]:
					dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
		return dp[m - 1][n - 1]
		
a = Solution()
word1 = "horse"; word2 = "ros"
word1 = "intention"; word2 = "execution"
print(a.minDistance(word1, word2))			
		
