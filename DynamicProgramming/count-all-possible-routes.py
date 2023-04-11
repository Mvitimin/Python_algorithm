from typing import List
from functools import lru_cache

class Solution:
	def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
		
		n = len(locations)
		MODULO = 10 ** 9 + 7
		
		@lru_cache(None)
		def dp(i, fuel):
		
			if fuel < 0:
				return 0
			
			val = 0
			for j in range(n):
				k = abs(locations[j] - locations[i])
				if i != j and k <= fuel:
					val += dp(j, fuel - k) + (1 if j == finish else 0)
			return val % MODULO
			
		return (dp(start, fuel) + (1 if start == finish else 0)) % MODULO

a = Solution()
locations = [2,3,6,8,4]; start = 1; finish = 3; fuel = 5
#locations = [4,3,1]; start = 1; finish = 0; fuel = 6
#locations = [5,2,1]; start = 0; finish = 2; fuel = 3
locations = [2,1,5]; start = 0; finish = 0; fuel = 3
print(a.countRoutes(locations, start, finish, fuel))
