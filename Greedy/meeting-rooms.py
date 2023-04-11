from typing import List

class Solution:
	def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
		intervals.sort(key = lambda x: x[0])
		if not intervals:
			return True
		for i in range(len(intervals) - 1):
			if intervals[i][1] > intervals[i + 1][0]:
				return False
		return True

a = Solution()
intervals = [[0,30],[5,10],[15,20]]
intervals = [[7,10],[2,4]]
print(a.canAttendMeetings(intervals))				
			
		
		
		
