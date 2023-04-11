from typing import List
from functools import lru_cache

class Solution:
	def probabilityOfHeads(self, prob: List[float], target: int) -> float:
		n = len(prob)
		
		@lru_cache(None)
		def dp(i, t):
			if i == n and t == 0:
				return 1
			if i == n or t < 0:
				return 0
			return (1 - prob[i]) * dp(i + 1, t) + prob[i] * dp(i + 1, t - 1)
			
		
		
		return round(dp(0, target), 5)	




prob = [0.5,0.5,0.5,0.5,0.5]; target = 5
prob = [0.4, 0.2]; target = 2
a = Solution()
print(a.probabilityOfHeads(prob, target))

