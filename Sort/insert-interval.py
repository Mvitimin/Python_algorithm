from typing import List
import collections
class Solution:
	def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
		ans = []
		ans = [newInterval]
		for s2, e2 in intervals:
			s1, e1 = ans.pop()
			if (e1 < s2) or (e2 < s1):
				ans.append([min(s1,s2), min(e1, e2)])
				ans.append([max(s1,s2), max(e1, e2)])
			else:
				ans.append([min(s1, s2), max(e1, e2)])	
		return ans 
	
a = Solution()		
intervals = [[1,3],[6,9]]; newInterval = [2,5]
print(a.insert(intervals, newInterval))
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]; newInterval = [4,8]
#intervals = []; newInterval = [5,7]	
#intervals = [[1,5]]; newInterval = [2,3]
#intervals = [[1,5]]; newInterval = [2,7]	
print(a.insert(intervals, newInterval))
						
			
			

