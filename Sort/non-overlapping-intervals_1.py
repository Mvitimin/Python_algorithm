from typing import List

class Solution:
	def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
		intervals.sort(key=lambda x : x[1])
		
		prev = float('-inf') 
		ans = 0
		for start, end in intervals:
			if start < prev:
				ans += 1
			else:
				prev = end
		return ans		
		
a = Solution()
intervals = [[1,2],[2,3],[3,4],[1,3]]
intervals = [[1,2],[1,2],[1,2]]
intervals = [[1,2],[2,3]]
print(a.eraseOverlapIntervals(intervals))
