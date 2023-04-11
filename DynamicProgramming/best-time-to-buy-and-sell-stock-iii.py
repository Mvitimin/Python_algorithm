from typing import List

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		n = len(prices)
		dp1 = [0] * (n + 1)
		dp2 = [0] * (n + 1)
		prev = prices[-1]
		ans = 0
		for i in range(n - 1, -1, -1):
			if prices[i] < prev:
				dp2[i] = max(dp2[i + 1], prev - prices[i])
			else:
				dp2[i] = dp2[i + 1]
			prev = max(prev, prices[i])
		prev = prices[0]
		for i in range(1, n):
			if prices[i] >= prev:
				dp1[i] = max(dp1[i - 1], prices[i] - prev)
			else:
				dp1[i] = dp1[i - 1]
			ans = max(ans, dp1[i - 1] + dp2[i])
			prev = min(prev, prices[i])
		return max(ans, max(dp1))
		
a = Solution()
prices = [3,3,5,0,0,3,1,4]
#prices = [1,2,3,4,5]
#prices = [1]
#prices = [7,6,4,3,1]
#prices = [0, 2, 3, 5, 3, 5, 6, 0]
#prices = [0, 3, 5, 2, 4, 3, 5, 6]
#prices = [1,2,4,2,5,7,2,4,9,0]
prices = [8,3,6,2,8,8,8,4,2,0,7,2,9,4,9]
print(a.maxProfit(prices))		
