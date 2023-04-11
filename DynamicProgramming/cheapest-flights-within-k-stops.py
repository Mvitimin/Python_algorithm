from typing import List
import collections
import heapq
class Solution:
	def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
		heap = [(0, 0, src)]
		graph = collections.defaultdict(list)
		visited = collections.defaultdict(lambda:float('inf'))
		ans = float('inf')
		for s, d, p in flights:
			graph[s].append((d, p))
		ans = float('inf')		
		while heap:
			cnt, price, node = heapq.heappop(heap)
			if cnt > K + 1: break
			if node == dst:
				ans = min(ans, price)
			for v, p in graph[node]:
				if visited[v] > p + price:
					visited[v] = p + price
					heapq.heappush(heap, (cnt + 1, p + price, v))
		
		return ans if ans != float('inf') else -1
			

a = Solution()
n = 3; flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0; dst = 2; k = 1
#n = 3; flights = [[0,1,100],[1,2,100],[0,2,500]]
#src = 0; dst = 2; k = 0
n = 4; flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0; dst = 3; k = 1

n = 5; flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
src = 0; dst = 2; k = 2
print(a.findCheapestPrice(n, flights, src, dst, k))
		
