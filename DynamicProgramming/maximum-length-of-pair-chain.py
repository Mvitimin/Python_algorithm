from typing import List
from functools import lru_cache

class Solution:
	def findLongestChain(self, pairs: List[List[int]]) -> int:
		n = len(pairs)
		pairs.sort()
		
		@lru_cache(None)
		def dp(i, prev):
			if i >= n: return 0		
			val = dp(i + 1, prev)
			if prev < pairs[i][0]:
				val = max(val, 1 + dp(i + 1, pairs[i][1]))
			return val 
		
		return dp(0, float('-inf'))		 
			
a = Solution()
pairs = [[1,2],[2,3],[3,4]]
pairs = [[1,2],[7,8],[4,5]]
print(a.findLongestChain(pairs))
