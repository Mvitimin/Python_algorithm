from typing import List
import heapq
import collections

class Solution:
	def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
		heap = []
		for i in range(n):
			heapq.heappush(heap, (0, i))
		meetings.sort()
		rooms = collections.defaultdict(int)		
		for start, end in meetings:
			while heap and heap[0][0] < start:
				e, idx = heapq.heappop(heap)
				heapq.heappush(heap, (start, idx))
			interval = end - start
			end, idx = heapq.heappop(heap)
			heapq.heappush(heap, (max(start, end) + interval, idx))
			rooms[idx] += 1
		return max(list(rooms.keys()), key=lambda x : rooms[x])
			
a = Solution()
n = 2; meetings = [[0,10],[1,5],[2,7],[3,4]]
n = 3; meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
n = 4; meetings = [[18,19],[3,12],[17,19],[2,13],[7,10]]
n = 4; meetings = [[19,20],[14,15],[13,14],[11,20]]
print(a.mostBooked(n, meetings))			
			
		
