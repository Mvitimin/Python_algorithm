from typing import List
import collections
class Solution:
	def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
		n, m = len(heights), len(heights[0])
		PACIFIC, ATLANTIC, BOTH = 1, 2, 3
		pacific = [(i, 0) for i in range(n)] + [(0, j) for j in range(m)] 
		atlantic = [(i, m - 1) for i in range(n)] + [(n - 1, j) for j in range(m)]	
		dx = [0, 0, 1, -1]
		dy = [1, -1, 0, 0]	
		colors = [[0] * m for _ in range(n)]
		ans = []
		def bfs(nodes, state):
			q = collections.deque(nodes)
			visited = set()
			for x, y in nodes:
				colors[x][y] |= state & BOTH
				visited.add((x, y))
			while q:
				x, y = q.popleft()
				for i in range(4):
					nx, ny = x + dx[i], y + dy[i]
					if 0 <= nx < n and 0 <= ny < m and heights[x][y] <= heights[nx][ny]:
						if (nx, ny) not in visited:
							visited.add((nx, ny))
							q.append((nx, ny))
							colors[nx][ny] |= state & BOTH
		
		bfs(pacific, PACIFIC) 
		bfs(atlantic, ATLANTIC)

		for i in range(n):
			for j in range(m):
				if colors[i][j] == BOTH:
					ans.append([i, j])
						
		return ans
						
a = Solution()
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
#heights = [[2,1],[1,2]]
#heights = [[10,10,10],[10,1,10],[10,10,10]]
print(a.pacificAtlantic(heights))

					
					
				



