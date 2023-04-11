from typing import List
class Solution:
	def stoneGame(self, piles: List[int]) -> bool:
		
		n = len(piles)
		dp = [[0] * (n + 1) for _ in range(n // 2 + 1)]
		
		for i in range(1, n // 2 + 1):
			for j in range(n):
				dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + piles[j], dp[i][j - 1])
		
		return sum(piles) - dp[n // 2][n - 1] * 2 < 0
		
				
a = Solution()
piles = [5, 3]

#piles = [3,7,2,3]
print(a.stoneGame(piles))		
				
				
				
				
				
			
