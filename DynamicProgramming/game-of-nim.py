from typing import List
from functools import lru_cache

class Solution:
	def nimGame(self, piles: List[int]) -> bool:
		n = len(piles)
		
		@lru_cache(None)
		def dp(num):
			num = list(num)
			for i in range(len(num)):
				for j in range(1, num[i] + 1):
					num[i] -= j
					if not dp(tuple(sorted(num))):
						return True
					num[i] += j
			return False 
		return dp(tuple(sorted(piles)))				
		
a = Solution()
piles = [1,2,3]
piles = [1,1]
piles = [1]
print(a.nimGame(piles))
