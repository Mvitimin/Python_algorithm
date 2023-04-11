from typing import List
import collections

class Solution:
	def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
		q = collections.deque([start])
		m, n = len(maze), len(maze[0])
		directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
		visited = set()
		visited.add((start[0], start[1]))
		while q:
			x, y = q.popleft()
			px, py = x, y
			for i in range(4):
				nx, ny = px, py 
				while 0 <= nx < m and 0 <= ny < n:
					if maze[nx][ny] == 1: break
					x, y = nx, ny
					nx, ny = nx + directions[i][0], ny + directions[i][1]
				if x == destination[0] and y == destination[1]:
					return True
				if (x, y) not in visited: 
					q.append((x, y))
					visited.add((x, y))
		return False
				
a = Solution()

#maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]; start = [0,4]; destination = [4,4]
#maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]; start = [0,4]; destination = [3,2]
maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]; start = [4,3]; destination = [0,1]
print(a.hasPath(maze, start, destination))
