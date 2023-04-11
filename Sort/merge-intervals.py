from typing import List

class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		intervals.sort(key=lambda x:x[0])
		start, end = intervals[0]
		ans = []
		for i in range(1, len(intervals)):
			if start <= intervals[i][0] <= end:
				end = max(end, intervals[i][1])
			else:
				ans += [start, end],
				start, end = intervals[i]
		ans.append([start, end])
		return ans

a = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
#intervals = [[1,4],[4,5]]
print(a.merge(intervals))				
