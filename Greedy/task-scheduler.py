from typing import List
import heapq
from collections import Counter
class Solution:
	def leastInterval(self, tasks: List[str], n: int) -> int:
		counter = Counter(tasks)
		heap, ans = [], []
		for task in counter:
			heapq.heappush(heap, (-counter[task], task))
		while heap:
			count, task = heapq.heappop(heap)
			ans.append(task)
			i, temp = 0, [] 
			while i < n and heap:
				ans.append(heap[0][1])
				temp.append(heap[0])
				heapq.heappop(heap)
				i += 1
			for item in temp:
				if item[0] + 1 != 0:
					heapq.heappush(heap, (item[0] + 1, item[1]))
				
			if count + 1 != 0:
				heapq.heappush(heap, (count + 1, task))	
				
			if heap:
				for k in range(i, n):
					ans.append("idle")
							
		return len(ans)

a = Solution()
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
tasks = ["A","A","A","B","B","B"]
n = 2
tasks = ["A","A","A","B","B","B"]
n = 0
print(a.leastInterval(tasks, n))
