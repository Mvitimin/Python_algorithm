from typing import List
from functools import lru_cache 
class Solution:
	def mergeStones(self, stones: List[int], K: int) -> int:
		@lru_cache(None)
		def dfs(l, r, piles):
			print(l, r, pile)
			if r - l + 1 < piles:
				return float('inf')
			if l == r:
				return 0			
			if piles == 1:
				return dfs(l, r, K) + sum(stones[l:r+1])
			return min(dfs(l, i, 1) + dfs(i + 1, r, piles - 1) for i in range(l, r))
		ans = dfs(0, len(stones) - 1, 1)
		return -1 if ans == float('inf') else ans
			

a = Solution()
#stones = [3,2,4,1]; k = 2
#stones = [3,2,4,1]; k = 3
#stones = [3,5,1,2,6]; k = 3
stones = [1, 2, 3, 4, 5, 6, 7]; k = 4
print(a.mergeStones(stones, k))
