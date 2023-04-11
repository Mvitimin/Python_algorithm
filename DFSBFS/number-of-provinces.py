import collections
from typing import List

class Solution:
	def findCircleNum(self, isConnected: List[List[int]]) -> int:
		n = len(isConnected)
		m = len(isConnected[0])
		graph = collections.defaultdict(list)
		for i in range(n):
			for j in range(m):
				if isConnected[i][j]:
					graph[i].append(j)
		
		visited = collections.defaultdict(int)
		group = 0
		def dfs(u, group):
			for v in graph[u]:
				if not visited[v]:
					visited[v] = group 
					dfs(v, group)
		
		for i in range(n):
			if not visited[i]:
				group += 1
				dfs(i, group)	
		#print(visited)
		return group	
			
a = Solution()
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
#isConnected = [[1,0,0],[0,1,0],[0,0,1]]
print(a.findCircleNum(isConnected))
			
					
