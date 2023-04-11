from typing import List

class Solution:
	def stoneGame(self, piles: List[int]) -> bool:
		n = len(piles)
		dp = [[0 for j in range(n)] for i in range(n)]
		dp[n - 1][n - 1] = piles[n - 1]
		for i in range(n - 2, -1 , -1):
			for j in range(i, n):
				if (j - i + 1) % 2 == 0: 
					dp[i][j] = max(piles[i] + dp[i + 1][j], piles[j] + dp[i][j - 1])
				else:
					dp[i][j] = min(-piles[i] + dp[i + 1][j], -piles[j] + dp[i][j - 1])
		return dp[0][n - 1] > 0

a = Solution()
piles = [5,3,4,5]

#piles = [4,8,9,4,2,5,7,10,5,7]
print(a.stoneGame(piles))
				

