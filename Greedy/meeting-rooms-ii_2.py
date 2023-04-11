from typing import List
import heapq
class Solution:
	def minMeetingRooms(self, intervals: List[List[int]]) -> int:
		intervals.sort(key=lambda x:x[0])
		heap = []
		ans = 1
		for start, end in intervals:
			while heap and start >= heap[0]:
				heapq.heappop(heap)
			heapq.heappush(heap, end)
			ans = max(ans, len(heap))
		return ans
				
				
a = Solution()
intervals = [[0,30],[5,10],[15,20]]
#intervals = [[7,10],[2,4]]
intervals = [[13,15],[1,13],[6,9]]
print(a.minMeetingRooms(intervals))
			
