
# Chronological Ordering
# https://leetcode.com/problems/meeting-rooms-ii/


from typing import List
import heapq

class Solution:
	def minMeetingRooms(self, intervals: List[List[int]]) -> int:
		starts = sorted([item[0] for item in intervals])		
		ends = sorted([item[1] for item in intervals])
		L, E, rooms = 0, 0, 0
		while L < len(starts):
			if starts[L] >= ends[E]:
				rooms -= 1
				E += 1
			
			rooms += 1
			L += 1
		return rooms

		
a = Solution()
#intervals = [[1, 10], [2, 7], [3, 19], [8, 12], [10, 20], [11, 30]]
intervals = [[0,30],[5,10],[15,20]]
print(a.minMeetingRooms(intervals))		
