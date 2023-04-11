from typing import List
import collections

class Solution:
	def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
		
		NOT_VSITIED, VISITED, DONE = 0, 1, 2
		graph = collections.defaultdict(list)
		visited = collections.defaultdict(int)
		for dest, src in prerequisites:
			graph[src].append(dest)
		ans = []
		def dfs(node):
			if visited[node] == VISITED:
				return False
			visited[node] = VISITED
			for v in graph[node]:
				if visited[v] != DONE:
					if not dfs(v):
						return False
			visited[node] = DONE
			ans.append(node)
			return True
		for i in range(numCourses):
			if visited[i] != DONE and not dfs(i):
				return []
		return ans[::-1]
		

a = Solution()
'''
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]	
'''
numCourses = 2
prerequisites = [[1,0]]
print(a.findOrder(numCourses, prerequisites))		
		
