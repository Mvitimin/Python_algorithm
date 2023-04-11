from functools import lru_cache
class Solution:
	def numTrees(self, n: int) -> int:
		
		@lru_cache(None)
		def dp(n):
			if n <= 1:
				return 1
			total = 0
			for i in range(1, n + 1):
				total += dp(i - 1) * dp(n - i)
			return total
		return dp(n)


a = Solution()
print(a.numTrees(5))			
			
			
			
