from typing import List
import heapq
import collections

class Solution:
	def minimumEffortPath(self, heights: List[List[int]]) -> int:
		dx = [1, -1, 0, 0]
		dy = [0, 0, 1, -1]
		heap, l_r, l_c = [], len(heights), len(heights[0])
		visited = collections.defaultdict(set)
		heapq.heappush(heap, (0, 0, 0))
		while heap:
			d, r, c = heapq.heappop(heap)
			if r == l_r - 1 and c == l_c - 1:
				return d
			for i in range(4):
				x, y = r + dx[i], c + dy[i]
				if 0 <= x < l_r and 0 <= y < l_c and (r, c) not in visited[(x, y)]:
					visited[(x, y)].add((r, c))
					heapq.heappush(heap, (max(d, abs(heights[r][c] - heights[x][y])), x, y))
		return 0

a = Solution()
#heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
#heights = [[1,2,3],[3,8,4],[5,3,5]]
heights = [[1,2,2],[3,8,2],[5,3,5]]
print(a.minimumEffortPath(heights))							
		
		
					
			
