from typing import List
import heapq

class Solution:
	def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
		heap = []
		for num, f, t in trips:
			heapq.heappush(heap, (f, num))
			heapq.heappush(heap, (t, -num))
		
		while heap:
			location, val = heapq.heappop(heap)
			capacity -= val 
			if capacity < 0: return False
		return True

a = Solution()
trips = [[2,1,5],[3,3,7]]; capacity = 4
#trips = [[2,1,5],[3,3,7]]; capacity = 5
#trips = [[2,1,5],[3,5,7]]; capacity = 3
print(a.carPooling(trips, capacity))
