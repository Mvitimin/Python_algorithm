from typing import List

class Solution:
	def maxProfit(self, prices: List[int]) -> int:	
		n = len(prices)
		buy1 = buy2 = -prices[0]
		t2 = t1 = 0
		for i in range(1, n):
			t2 = max(t2, prices[i] + buy2)
			buy2 = max(buy2, t1 - prices[i])		
			t1 = max(t1, prices[i] + buy1)
			buy1 = max(buy1, -prices[i])		
		return t2

a = Solution()
prices = [3,3,5,0,0,3,1,4]
prices = [1,2,3,4,5]
#prices = [7,6,4,3,1]
#prices = [1]
#prices = [3,2,6,5,0,3]
print(a.maxProfit(prices))
			
				
