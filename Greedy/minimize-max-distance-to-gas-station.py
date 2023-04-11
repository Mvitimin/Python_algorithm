from typing import List
import heapq

class Solution:
	def minmaxGasDist(self, stations: List[int], k: int) -> float:
		n = len(stations)
		heap = []
		for i in range(n - 1):
			heapq.heappush(heap, (stations[i] - stations[i + 1], stations[i + 1] - stations[i], 1))
		
		for _ in range(k):
			dist, org, cnt = heapq.heappop(heap)
			cnt += 1
			heapq.heappush(heap, (-org / cnt, org, cnt))		
		
		return -round(heap[0][0], 5)
		

a = Solution()
stations = [1,2,3,4,5,6,7,8,9,10]; k = 9
#stations = [23,24,36,39,46,56,57,65,84,98]; k = 1
#stations = [10,19,25,27,56,63,70,87,96,97]; k = 3
#stations = [13,15,20,31,46,49,51,52,67,87]; k =7
print(a.minmaxGasDist(stations, k))
