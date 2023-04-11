import math
from functools import lru_cache
class Solution:
	def numSquares(self, n: int) -> int:
		
		@lru_cache(None)
		def solve(n):
			if n == 0:
				return 0
			val = float('inf')
			for i in range(int(math.sqrt(n)), 0, -1):
				val = min(val, n // (i * i) + solve(n % (i * i)))
			return val 
		
		return solve(n)
					
			


a = Solution()
n = 10 ** 3
print(a.numSquares(n))	

