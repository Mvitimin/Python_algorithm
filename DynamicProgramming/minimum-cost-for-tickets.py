from typing import List
from functools import lru_cache

class Solution:
	def mincostTickets(self, days: List[int], costs: List[int]) -> int:
		n = len(days)
		durations = [1, 7, 30]
		
		@lru_cache(None)
		def dp(i):
			if i >= n: return 0
			val = float('inf')
			for d, c in zip(durations, costs):
				idx = i
				while idx < n and days[idx] < days[i] + d:
					idx += 1
				val = min(val, dp(idx) + c)
			return val
		return dp(0)			
				
			
										
																			
days = [1,4,6,7,8,20]; costs = [2,7,15]
days = [1,2,3,4,5,6,7,8,9,10,30,31]; costs = [2,7,15]
days = [1,4,6,7,8,20]; costs = [7,2,15]
#print(bisect.bisect_left(days, 3))				
a = Solution()
print(a.mincostTickets(days, costs))				

