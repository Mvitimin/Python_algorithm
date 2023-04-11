from typing import List
import collections

class Solution:
	def leastInterval(self, tasks: List[str], n: int) -> int:
		counter = collections.Counter(tasks)
		maxTask = max(counter, key=lambda x:counter[x])
		bucket = counter[maxTask] - 1
		spaces = n * bucket
		for t in counter:
			if t == maxTask: continue
			spaces -= min(bucket, counter[t])
		return len(tasks) + max(spaces, 0)			
			
			
			
			
		


a = Solution()
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]; n = 2
tasks = ["A","A","A","B","B","B"]; n = 2
tasks = ["A","A","A","B","B","B"]; n = 0
#tasks = ["A", "A", "B", "B"]; n = 2
#tasks =["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]; n = 2
ans = a.leastInterval(tasks, n)
print(ans)
