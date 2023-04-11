from typing import List
from functools import lru_cache
class Solution:
	def stoneGameII(self, piles: List[int]) -> int:
		N = len(piles)
		
		@lru_cache(None)
		def dp(i, m, alice):
			if i > N:
				return 0	
			if alice:
				return max([sum(piles[i:i + j]) + dp(i + j, max(j, m), False) for j in range(1, 2 * m + 1)])
			else:
				return min([-sum(piles[i:i + j]) + dp(i + j, max(j, m), True) for j in range(1, 2 * m + 1)])
		return (dp(0, 1, True) + sum(piles)) // 2


piles = [2,7,9,4,4]
piles = [1,2,3,4,5,100]
a = Solution()
print(a.stoneGameII(piles))			
