from typing import List
class Solution:
	def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
		
		intervals.sort(key=lambda x:x[1])
		end = float('-inf')
		ans = 0
		
		for s, e in intervals:
			if s < end:
				ans += 1
			else:
				end = e
		return ans
	
a = Solution()
intervals = [[1,2],[2,3],[3,4],[1,3]]
#intervals = [[1,2],[1,2],[1,2]]
intervals = [[1,2],[2,3]]
print(a.eraseOverlapIntervals(intervals))
