from typing import List
class Solution:
	def minMeetingRooms(self, intervals: List[List[int]]) -> int:
		time_list = []
		intervals.sort(key=lambda x:x[0])
		for i in range(len(intervals)):
			time_list.append((intervals[i][0], 0, i))
			time_list.append((intervals[i][1], 1, i))
		
		time_list.sort(key=lambda x:x[0])
		meetings = set()
		ans = 0
		for i in range(len(time_list)):
			if time_list[i][1] == 0:
				meetings.add(time_list[i][2])
			else:
				meetings.remove(time_list[i][2])
			ans = max(ans, len(meetings))
		
		return ans


a = Solution()
intervals = [[0,30],[5,10],[15,20]]
intervals = [[7,10],[2,4]]
intervals = [[13,15],[1,13]]
print(a.minMeetingRooms(intervals))
