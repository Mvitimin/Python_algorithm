from functools import lru_cache
from typing import List

class Solution:
	def maxProfit(self, k: int, prices: List[int]) -> int:
		n = len(prices)
		@lru_cache(None)
		def dp(i, cnt, status):
			if cnt <= 0 or i >= n: return 0				
			val = dp(i + 1, cnt, status)
			if status == 1:
				val = max(val, prices[i] + dp(i, cnt - 1, 0))
			elif status == 0:
				val = max(val, -prices[i] + dp(i, cnt, 1)) 
			return val		
		return dp(0, k, 0)			

a = Solution()
k = 2; prices = [2,4,1]
k = 2; prices = [3,2,6,5,0,3]
print(a.maxProfit(k, prices))
					
			
