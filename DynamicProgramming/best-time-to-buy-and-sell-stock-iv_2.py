class Solution:
	def maxProfit(self, k: int, prices: List[int]) -> int:
		if not k:
			return k
		t_cost = [float('inf')] * k
		t_profit = [0] * k
		
		for price in prices:
			t_cost[0] = min(t_cost[0], price)
			t_profit[0] = max(t_profit[0], price - t_cost[0])
			for i in range(1, k):
				t_cost[i] = min(t_cost[i], price - t_profit[i - 1])
				t_profit[i] = max(t_profit[i], price - t_cost[i])
				
		return t_profit[-1]
