from typing import List
from functools import lru_cache
class Solution:
	def lastStoneWeightII(self, stones: List[int]) -> int:
		n = len(stones)
		
		@lru_cache(None)
		def helper(index, a, b):
			if index >= n:
				return abs(a - b)
			return min(helper(index + 1, a + stones[index], b),
			helper(index + 1, a, b + stones[index]))
		return helper(0, 0, 0)

a = Solution()
stones = [2,7,4,1,8,1]
stones = [31,26,33,21,40]
stones = [1,2]
print(a.lastStoneWeightII(stones))
