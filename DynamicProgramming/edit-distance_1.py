from functools import lru_cache
class Solution:
	def minDistance(self, word1: str, word2: str) -> int:
		n, m = len(word1), len(word2)
		dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
		dp[0] = [i for i in range(m + 1)]
		
		for i in range(1, n + 1):
			for j in range(m + 1):
				if j == 0:
					dp[i][j] = i
					continue
				dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
				if word1[i - 1] == word2[j - 1]:
					dp[i][j] = min(dp[i][j], dp[i - 1][j - 1])
		print(dp)
		return dp[-1][-1]
	
a = Solution()
word1 = "horse"; word2 = "ros"	
#word1 = "b"; word2 = "abc"
#word1 = "intention"; word2 = "execution"
print(a.minDistance(word1, word2))			
			


