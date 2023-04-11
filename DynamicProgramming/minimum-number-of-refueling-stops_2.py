from typing import List
import heapq
class Solution:
	def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
		stations.append((target, float('inf')))
		fuel, prev = startFuel, 0
		heap = []
		location = ans = 0
		for d, f in stations:
			location += d - prev 	
			while heap and fuel - location < 0:
				fuel -= heapq.heappop(heap)
				ans += 1
			if fuel - location < 0: return  -1 
			heapq.heappush(heap, -f)
			prev = d
		return ans
			
		
		
							
											
a = Solution()
#target = 100; startFuel = 10; stations = [[10,60],[20,30],[30,30],[60,40]]
#target = 200; startFuel = 50; stations = [[25,25],[50,100],[100,100],[150,40]]
#target = 100; startFuel = 1; stations = [[10,100]]
#target = 1; startFuel = 1; stations = []
print(a.minRefuelStops(target, startFuel, stations))
