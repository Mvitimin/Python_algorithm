from typing import List
from functools import lru_cache

class Solution:
	def stoneGameVII(self, stones: List[int]) -> int:
		n = len(stones)
		s = sum(stones)
		@lru_cache(None)
		def dp(i, j):
			if (j - i + 1) <= 1:
				return 0		
			return max(min(stones[j] + dp(i + 1, j - 1), stones[i + 1] + dp(i + 2, j)),
			min(stones[i] + dp(i + 1, j - 1), stones[j - 1] + dp(i, j - 2)))
		return dp(0, n - 1)
		
			
a = Solution()		
stones = [5,3,1,4,2]
#stones = [7,90,5,1,100,10,10,2]
print(a.stoneGameVII(stones))
