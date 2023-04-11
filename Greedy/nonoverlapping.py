
from typing import List

class Solution:
	def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
		intervals.sort(key=lambda x : (x[1]))
		print(intervals)
		start = float('-inf')
		ans = 0
		for i, j in intervals:
			if i < start:
				ans += 1
			else: start = j 
		return ans 			
			
a = Solution()
intervals = [[1, 2], [2, 3], [3, 8], [4, 5], [6, 7]]	
a.eraseOverlapIntervals(intervals)
