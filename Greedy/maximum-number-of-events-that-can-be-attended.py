from typing import List
import heapq

class Solution:
	def maxEvents(self, events: List[List[int]]) -> int:
		events.sort()
		max_day = max(events, key=lambda x: x[1])
		heap = []
		ans = i = 0
		for day in range(1, max_day[1] + 1):
			while i < len(events) and events[i][0] == day:
				heapq.heappush(heap, (events[i][1]))
				i += 1
			while heap and day > heap[0]:
				heapq.heappop(heap)
			if heap:
				heapq.heappop(heap)
				ans += 1			
		return ans		
#events= [[1,2],[2,3],[3,4],[1,2]]
#events = [[1,2],[2,3],[3,4]]
#events = [[1, 3], [3, 4], [1, 4]]
#events = [[1, 1], [1, 3]]
#events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
#events = [[1,2],[1,2],[1,6],[1,2],[1,2]]
#events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
events =[[1,2],[1,2],[3,3],[1,5],[1,5]]
#events  = [[1,5],[1,5],[1,5],[2,3],[2,3]]
a = Solution()
print(a.maxEvents(events))
