from functools import lru_cache

class Solution:
	def integerReplacement(self, n: int) -> int:
		@lru_cache(None)
		def solve(m):
			if m <= 1: return 0
			if m % 2 == 0: return 1 + solve(m // 2)
			else: return 1 + min(solve(m + 1), solve(m - 1))
		return solve(n)

a = Solution()
i = 1234
print(i, a.integerReplacement(i))
	
