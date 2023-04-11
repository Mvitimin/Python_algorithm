from typing import List

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		buy = prices[0] 
		ans = 0
		for i in range(1, len(prices)):
			ans = max(ans, prices[i] - buy)
			buy = min(prices[i], buy)
		return ans

a = Solution()
prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
print(a.maxProfit(prices))
