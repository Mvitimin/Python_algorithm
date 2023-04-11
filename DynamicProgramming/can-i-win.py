from functools import lru_cache
class Solution:
	def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
		if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
			return False
		if maxChoosableInteger >= desiredTotal:
			return True
		
		@lru_cache(None)
		def helper(selectedCards, total):
			return any(max(selectedCards) + total >= desiredTotal or not helper(frozenset(selectedCards - {card}), total + card) for card in selectedCards)
			
		return helper(frozenset(range(1, maxChoosableInteger + 1)), 0)
	
a = Solution()
#maxChoosableInteger = 4; desiredTotal = 6
#maxChoosableInteger = 10; desiredTotal = 11
maxChoosableInteger = 10; desiredTotal = 40
print(a.canIWin(maxChoosableInteger, desiredTotal))			
				
		

