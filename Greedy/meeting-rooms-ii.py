
#Heap 
# https://leetcode.com/problems/meeting-rooms-ii/


from typing import List
import heapq

class Solution:
	def minMeetingRooms(self, intervals: List[List[int]]) -> int:
		
		L, heap = len(intervals), []
		intervals.sort(key=lambda x: x[0])
		for i in range(L):
			
			if heap and intervals[i][0] >= heap[0]:
				heapq.heappop(heap)
			heapq.heappush(heap, intervals[i][1])	
			
		return len(heap)
		

		
a = Solution()
intervals = [[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]]
#intervals = [[0,30],[5,10],[15,20]]
print(a.minMeetingRooms(intervals))		
