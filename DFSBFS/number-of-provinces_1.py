from typing import List
import collections


class Solution:
	def findCircleNum(self, isConnected: List[List[int]]) -> int:
		graph = collections.defaultdict(list)
		
		n = len(isConnected)
		
		for i in range(n):
			for j in range(n):
				if isConnected[i][j]:
					graph[i].append(j)
		
		
		visited = [False] * n
		
		def dfs(u):
			visited[u] = True
			for v in graph[u]:
				if not visited[v]:
					dfs(v)
		
		ans = 0
		for i in range(n):
			if not visited[i]:
				dfs(i)	
				ans += 1
		return ans
		

a = Solution()
isConnected = [[1,1,0],[1,1,0],[0,0,1]]	
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
print(a.findCircleNum(isConnected))			
			
			

