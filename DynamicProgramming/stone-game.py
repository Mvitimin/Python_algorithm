from typing import List

class Solution:
	def stoneGame(self, piles: List[int]) -> bool:
		N = len(piles)
		dp = [[0] * N for _ in range(N)]
		dp[N - 1][N - 1] = piles[N - 1]
		for i in range(N - 2, -1, -1):
			for j in range(i, N):
				if (j - i + 1) % 2 == 0:
					dp[i][j] = max(piles[i] + dp[i + 1][j], piles[j] + dp[i][j - 1])
				else:
					dp[i][j] = min(-piles[i] + dp[i + 1][j], -piles[j] + dp[i][j - 1])			
		return dp[0][N - 1] > 0
								
a = Solution()
piles = [5, 7, 0, 1, 4, 4]
#piles = [5,3,4,5]
#piles = [7,8,8,10]
piles = [8,9,7,6,7,6]
print(a.stoneGame(piles))
				
		
