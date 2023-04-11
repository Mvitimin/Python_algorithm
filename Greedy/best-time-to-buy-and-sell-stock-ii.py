from typing import List

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		ans = 0
		for i in range(len(prices) - 1):
			if prices[i] < prices[i + 1]:
				ans += prices[i + 1] - prices[i]
		return ans	
		
a = Solution()
prices = [7,1,5,3,6,4]
prices = [1,2,3,4,5]
#prices = [7,6,4,3,1]
print(a.maxProfit(prices))
