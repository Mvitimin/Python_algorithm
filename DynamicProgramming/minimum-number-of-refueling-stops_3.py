from typing import List
class Solution:
	def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
		n = len(stations)
		dp = [startFuel] * (n + 1)
		stations = [[0, 0]] + stations
		
		for i, (d, f) in enumerate(stations):
			for j in range(i - 1, -1, -1):
				if dp[j] >= d:
					dp[j + 1]= max(dp[j + 1], dp[j] + f)
		
		for i, d in enumerate(dp):
			if d >= target: return i 
		
		return -1
		
			
a = Solution()
target = 100; startFuel = 10; stations = [[10,60],[20,30],[30,30],[60,40]]
target = 100; startFuel = 1; stations = [[10,100]]
#target = 1; startFuel = 1; stations = []
#target = 100; startFuel = 50; stations = [[25,25],[50,50]]
print(a.minRefuelStops(target, startFuel, stations))
