from typing import List
import collections

class Solution:
	def removeStones(self, stones: List[List[int]]) -> int:
		cols = collections.defaultdict(set)
		rows = collections.defaultdict(set)
		
		for x, y in stones:
			rows[x].add((x, y))
			cols[y].add((x, y))
	
		def dfs(cell):
			rows[cell[0]].remove(cell)
			cols[cell[1]].remove(cell)
			for stone in (cols[cell[1]] | rows[cell[0]]):
				if stone in cols[cell[1]] or stone in rows[cell[0]]:
					dfs(stone)
		
		n, ans = len(stones), 0
		for x, y in stones:
			stone = (x, y)
			if stone in cols[y] or stone in rows[x]:
				dfs(stone)
				ans += 1
		
		return n - ans
		
			
a = Solution()
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
print(a.removeStones(stones))

print(~1)
print(~2)
print(~3)
