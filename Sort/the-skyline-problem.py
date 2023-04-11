import heapq
from typing import List

class Solution:
	def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
		events = []
		for L, R, H in buildings:
			events += [[L, -H, R]]
			events += [[R, 0, 0]]
		events.sort()
		ans, heap = [(0, 0)], [(0, float('inf'))]
		
		for L, nH, R in events:
			
			while heap[0][1] <= L:
				heapq.heappop(heap)
			
			if nH != 0: heapq.heappush(heap, (nH, R))
			
			if ans[-1][1] != -heap[0][0]:
				ans.append([L, -heap[0][0]])  
		return ans[1:]

buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]			 
		
a = Solution()
print(a.getSkyline(buildings))			
