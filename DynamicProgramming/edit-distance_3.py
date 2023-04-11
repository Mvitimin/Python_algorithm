class Solution:
	def minDistance(self, word1: str, word2: str) -> int:
		m, n = len(word1), len(word2)
		dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
		
		for i in range(m + 1):
			dp[i][0] = i 	
		for j in range(n + 1):
			dp[0][j] = j 
		
		
		for i, c1 in enumerate(word1, 1):
			for j, c2 in enumerate(word2, 1):
				dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + (0 if c1 == c2 else 1), dp[i - 1][j] + 1, dp[i][j - 1] + 1)
		
		'''
		for i in range(m + 1):
			print(dp[i])
			print()
		'''
		
		return dp[-1][-1]


word1 = 'horse'; word2 = 'ros'
word1 = "intention"; word2 = "execution"
a = Solution()
print(a.minDistance(word1, word2))
