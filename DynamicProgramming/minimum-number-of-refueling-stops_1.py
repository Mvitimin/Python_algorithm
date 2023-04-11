from typing import List
import heapq
class Solution:
	def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
		n = len(stations)
		heap = [(0, -1, startFuel)]
		visited = [0] * (n + 1)
		stations.append([0, 0])
		
		while heap:
			cnt, index, fuel = heapq.heappop(heap)
			
			if stations[index][0] + fuel >= target:
				#print(visited)			
				return cnt
			
			for i in range(n, index, - 1):
				dst = stations[i][0] - stations[index][0]
				f = fuel - dst + stations[i][1]
				if fuel >= dst and visited[i] <= f:
					visited[i] = f
					heapq.heappush(heap, (cnt + 1, i, f))
		return -1
									
											
a = Solution()
target = 100; startFuel = 10; stations = [[10,60],[20,30],[30,30],[60,40]]
target = 200; startFuel = 50; stations = [[25,25],[50,100],[100,100],[150,40]]
#target = 100; startFuel = 1; stations = [[10,100]]
#target = 1; startFuel = 1; stations = []
print(a.minRefuelStops(target, startFuel, stations))
