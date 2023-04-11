from typing import List
import collections

class Solution:
	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		path = [False] * numCourses
		checked = [False] * numCourses
		graph = collections.defaultdict(list)
		
		for dest, src in prerequisites:
			graph[src].append(dest)
		
		def isCyclic(node):
			
			if checked[node]:
				return False
			if path[node]: 
				return True
			
			path[node] = True	
			res = False
			for v in graph[node]:
				res = isCyclic(v)
				if res:
					return res
			
			path[node] = False
			checked[node] = True
			return res
	
		for i in range(numCourses):
			if isCyclic(i):
				return False
		return True

a = Solution()
#numCourses = 2
#prerequisites = [[1,0],[0,1]]
numCourses = 2
prerequisites = [[1,0]]
print(a.canFinish(numCourses, prerequisites))	
		
				
