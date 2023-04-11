from typing import List
from functools import lru_cache

class Solution:
	def stoneGame(self, piles: List[int]) -> bool:
		total = sum(piles)
		@lru_cache(None)
		def dp(i, j):
			if j - i + 1 <= 2:
				return max(piles[i], piles[j])
			return max(piles[i] + dp(i + 2, j),
			piles[i] + dp(i + 1, j - 1),
			piles[j] + dp(i, j - 2),
			piles[j] + dp(i + 1, j - 1))		
		return total - dp(0, len(piles) - 1) < total // 2
			
a = Solution()
piles = [5, 7, 0, 1, 4, 4]
#piles = [5,3,4,5]
#piles = [7,8,8,10]
piles = [8,9,7,6,7,6]
print(a.stoneGame(piles))
				
		

