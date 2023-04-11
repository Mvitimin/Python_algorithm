from typing import List
from collections import Counter
class Solution:
	def leastInterval(self, tasks: List[str], n: int) -> int:
		counter = Counter(tasks)
		frequencies = list(counter.values())
		frequencies.sort()
		max_freq = frequencies.pop()
		idle = (max_freq - 1)	* n
						
		while idle > 0 and frequencies: 
			idle -= min(max_freq - 1, frequencies.pop())
			
		idle = max(idle, 0)
			
		return len(tasks) + idle

a = Solution()
tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
n = 2
#tasks = ["A","A","A","B","B","B"]
#n = 2
#tasks = ["A","A","A","B","B","B"]
#n = 0
print(a.leastInterval(tasks, n))
