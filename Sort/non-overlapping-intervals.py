
from typing import List

class Solution:
	def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
		intervals.sort(key=lambda x : (x[1]))
		start = float('-inf')
		ans = 0
		for i, j in intervals:
			if i < start:
				ans += 1
			else: start = j 
		print(intervals)
		return ans 			
			
			
a = Solution()
intervals = [[1,3],[2,3],[3,4],[1,2]]
intervals = [[1,2],[1,2],[1,2]]
intervals = [[1,2],[2,3]]
intervals = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
print(a.eraseOverlapIntervals(intervals))
