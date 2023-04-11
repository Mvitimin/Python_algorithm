from typing import List
from functools import lru_cache
class Solution:
	def lastStoneWeightII(self, stones: List[int]) -> int:
		n = len(stones)
		total = sum(stones)
		@lru_cache(None)
		def helper(index, a):
			if index >= n:
				return abs(total - 2 * a) 
			return min(helper(index + 1, a + stones[index]),
			helper(index + 1, a))
		return helper(0, 0)
		
stones = [2,7,4,1,8,1]
stones = [31,26,33,21,40]
a = Solution()
print(a.lastStoneWeightII(stones))
