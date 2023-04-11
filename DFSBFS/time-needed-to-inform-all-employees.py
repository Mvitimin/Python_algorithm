import collections
from typing import List
class Solution:
	def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
		
		graph = collections.defaultdict(list)
		q = collections.deque([(headID, 0)])
		
		for i in range(n):
			graph[manager[i]].append(i)
		
		ans = 0
				
		while q:	
			u, time = q.popleft()
			ans = max(ans, time)		
			for v in graph[u]:
				q.append((v, time + informTime[u]))
		return ans

			
				
				
				
a = Solution()
n = 6; headID = 2; manager = [2,2,-1,2,2,2]; informTime = [0,0,1,0,0,0]	
n = 1; headID = 0; manager = [-1]; informTime = [0]
print(a.numOfMinutes(n, headID, manager, informTime))
			
		
						
