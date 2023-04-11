from typing import List

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		n = len(prices)
		held = -prices[0] # buy
		nothing = 0 # nothing
		prev = sold = 0 # sell
		for i in range(1, n):
			prev = sold
			sold = max(sold, held + prices[i])
			held = max(held, nothing - prices[i])
			nothing = prev
		return sold

a = Solution()
prices = [1,2,3,0,2]
prices = [2, 1]
#prices = [2, 1, 4]
print(a.maxProfit(prices))
