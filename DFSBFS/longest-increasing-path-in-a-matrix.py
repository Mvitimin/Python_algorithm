from typing import List
import heapq
import collections
class Solution:
	def longestIncreasingPath(self, matrix: List[List[int]]) -> int:	
		nodes = []
		dx = [-1, 1, 0, 0]
		dy = [0, 0, -1, 1]
		n, m = len(matrix), len(matrix[0])
		dists = {}	
		for i in range(n):
			for j in range(m):
				nodes.append((matrix[i][j], i, j))
		nodes.sort(key=lambda x : x[0], reverse=True)
		
		def findPath(x, y):
			heap = []
			heapq.heappush(heap, (0, x, y))
			visited = collections.defaultdict(lambda:float('inf'))
			visited[(x, y)] = 0
			max_dist = 1
			while heap:
				d, x, y = heapq.heappop(heap)
				if visited[(x, y)] < d:
					continue
				if (x, y) in dists:
					max_dist = max(max_dist, -d + dists[(x, y)])
					continue
				max_dist = max(max_dist, -d)
				for i in range(4):
					nx, ny = dx[i] + x, dy[i] + y 
					if 0 <= nx < n and 0 <= ny < m and matrix[x][y] < matrix[nx][ny]:
						if visited[(nx, ny)] > d - 1:
							visited[(nx, ny)] = d - 1
							heapq.heappush(heap, (d - 1, nx, ny))
						
			return max_dist
		
		for val, i, j in nodes:
			dists[(i, j)] = findPath(i, j)
		return max(dists.values())


a = Solution()
matrix = [[9,9,4],[6,6,8],[2,1,1]]
matrix = [[3,4,5],[3,2,6],[2,2,1]]
matrix = [[1]]
print(a.longestIncreasingPath(matrix))
