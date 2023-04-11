from typing import List
import heapq
class Solution:
	def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
		events = []
		ans = [-1] * len(workers)
		occupied = set()
		for i, p1 in enumerate(workers):
			for j, p2 in enumerate(bikes):
				events.append([abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]), i, j])
		events.sort(reverse=True)
		while events:
			d, worker, bike = events.pop()
			if ans[worker] == -1 and bike not in occupied:
				ans[worker] = bike
				occupied.add(bike)	
		return ans

a = Solution()
workers = [[0,0],[2,1]]; bikes = [[1,2],[3,3]]
workers = [[0,0],[1,1],[2,0]]; bikes = [[1,0],[2,2],[2,1]]
print(a.assignBikes(workers, bikes))				
