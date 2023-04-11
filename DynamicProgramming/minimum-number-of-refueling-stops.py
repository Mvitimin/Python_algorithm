from typing import List
from functools import lru_cache 
class Solution:
	def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
		stations.insert(0, [0, 0])
		n = len(stations)
		
		@lru_cache(None)
		def dp(i, fuel):
			if stations[i][0] + fuel >= target: return 0			
			val = float('inf')
			for j in range(i + 1, n):
				if stations[j][0] <= stations[i][0] + fuel:
					val = min(val, 1 + dp(j, fuel - (stations[j][0] - stations[i][0]) + stations[j][1]))
			return val	
		ans = dp(0, startFuel)
		return ans if ans != float('inf') else -1
			
a = Solution()
target = 100; startFuel = 10; stations = [[10,60],[20,30],[30,30],[60,40]]
target = 100; startFuel = 1; stations = [[10,100]]
target = 1; startFuel = 1; stations = []
print(a.minRefuelStops(target, startFuel, stations))
