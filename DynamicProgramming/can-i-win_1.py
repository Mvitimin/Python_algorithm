from functools import lru_cache

class Solution:
	def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
		@lru_cache(None)
		def dp(choosable, total):
			if sum(choosable) < total:
				return False
			if max(choosable) >= total:
				return True

			return any(not dp(tuple(choosable[:i] + choosable[i+1:]), total - choosable[i]) for i in range(len(choosable)))
		return dp(tuple(range (1, maxChoosableInteger + 1)), desiredTotal)
		
a = Solution()
maxChoosableInteger = 10; desiredTotal = 11
maxChoosableInteger = 10; desiredTotal = 0
maxChoosableInteger = 10; desiredTotal = 1
print(a.canIWin(maxChoosableInteger, desiredTotal))		
		
