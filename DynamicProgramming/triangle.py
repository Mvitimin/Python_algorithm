from typing import List
from functools import lru_cache

class Solution:
	def minimumTotal(self, triangle: List[List[int]]) -> int:
		n = len(triangle)
		
		@lru_cache(None)
		def dp(row, i):
			if row >= n:
				return 0 
			return triangle[row][i] + min(dp(row + 1, i), dp(row + 1, i + 1))
		return dp(0, 0)
			

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[-10]]
a = Solution()
print(a.minimumTotal(triangle))
