from functools import lru_cache

class Solution:
	def getMoneyAmount(self, n: int) -> int:
		
		@lru_cache(None)
		def dp(left, right):
			if left >= right:
				return 0
			
			val = float('inf')
			for i in range(left, right + 1):
				val = min(val, i + max(dp(i + 1, right), dp(left, i - 1)))
			return val
		return dp(1, n) 

a = Solution()
n = 10
print(a.getMoneyAmount(n))
