from typing import List
import collections
class Solution:
	def numberOfCleanRooms(self, room: List[List[int]]) -> int:
		# right, down, left, up
		directions = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
		visited = set()
		seen = set()
		m, n = len(room), len(room[0])
		q = collections.deque([(0, 0, 0)])
		while q:
			x, y, d = q.popleft()
			if (x, y) not in seen:
				seen.add((x, y))
			visited.add((x, y, d))
			for i in range(4):
				new_d = (d + i) % 4
				nx, ny = x + directions[new_d][0], y + directions[new_d][1]
				if 0 <= nx < m and 0 <= ny < n and room[nx][ny] == 0:
					if (nx, ny, new_d) not in visited:
						q.append((nx, ny, new_d))
					break
		return len(seen)
		

a = Solution() 
room = [[0,0,0],[1,1,0],[0,0,0]]
room = [[0,1,0],[1,0,0],[0,0,0]]
#room = [[0,0,0],[0,0,0],[0,0,0]]
#room = [[0,0,0,1],[0,1,0,1],[1,0,0,0]]
room = [[0,0,0],[0,0,1]]
print(a.numberOfCleanRooms(room))	
					
								
			
		

