from typing import List

class Solution:
	def stoneGameII(self, piles: List[int]) -> int:
		N = len(piles)
		for i in range(N - 2, -1, -1):
			piles[i] += piles[i + 1]
		
		dp = [[0] * (N + 1) for _ in range(N)]
		for i in range(N - 1, -1, -1):
			for m in range(N, 0, -1):
				for x in range(1, 2 * m + 1):
					val = piles[i] - dp[i + x][max(x, m)] if i + x < N else piles[i]
					dp[i][m] = max(dp[i][m], val)
		return dp[0][1]
		
a = Solution()
piles = [1]
piles = [2,7,9,4,4]
piles = [1,2,3,4,5,100]
print(a.stoneGameII(piles))
					

