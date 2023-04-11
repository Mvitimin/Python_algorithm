from functools import lru_cache

class Solution:
	def winnerSquareGame(self, n: int) -> bool:
		
		@lru_cache(None)
		def helper(num):	
			if num == 0:
				return False 	
			val = int(num ** 0.5)
			if val ** 2 == num:
				return True
			for i in range(1, val + 1):
				if not helper(num - i * i):
					return True
			return False			
		return helper(n)
	

a = Solution()
n = 1
n = 2
n = 4
n = 7
n = 17
n = 19
print(a.winnerSquareGame(n))
	
