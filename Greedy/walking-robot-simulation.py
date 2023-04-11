from typing import List

class Solution:
	def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
		move = [(0, 1), (1, 0), (0, -1), (-1, 0)] # N -> E -> S -> W
		obstacles_set = set([(obstacles[i][0], obstacles[i][1]) for i in range(len(obstacles))])
		x = y = 0
		direction = 0
		ans = 0
		for command in commands:
			if command == -2:
				direction = (direction - 1) % 4
			elif command == -1:
				direction = (direction + 1) % 4
			else:
				for _ in range(command):
					nx, ny = x + move[direction][0], y + move[direction][1]
					if (nx, ny) in obstacles_set:
						break	
					x, y = nx, ny
				ans = max(ans, x ** 2 + y ** 2)
		return ans
		
a = Solution()
commands = [4,-1,3]; obstacles = []
commands = [4,-1,4,-2,4]; obstacles = [[2,4]]
ans = a.robotSim(commands, obstacles)
print(ans)
			
						
				
				
