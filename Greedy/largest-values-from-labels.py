from typing import List
import collections
import heapq

class Solution: 
	def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
		heap = []
		n = len(values)
		counter = collections.defaultdict(int)
		for i in range(n):
			heapq.heappush(heap, (-values[i], labels[i]))
		
		ans = 0
		while heap and numWanted > 0:
			
			x, l = heapq.heappop(heap)
			if counter[l] >= useLimit:
				continue
			ans -= x
			numWanted -= 1
			counter[l] += 1
		return ans
	
			
a = Solution()
values = [5,4,3,2,1]; labels = [1,1,2,2,3]; numWanted = 3; useLimit = 1		
values = [5,4,3,2,1]; labels = [1,3,3,3,2]; numWanted = 3; useLimit = 2	
values = [9,8,8,7,6]; labels = [0,0,0,1,1]; numWanted = 3; useLimit = 1
print(a.largestValsFromLabels(values, labels, numWanted, useLimit))
		
		
