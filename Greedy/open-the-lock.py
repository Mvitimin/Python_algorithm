import collections
from typing import List

class Solution:
	def openLock(self, deadends: List[str], target: str) -> int:
		visited = set(deadends)	
		q = collections.deque([('0000', 0)])
		if '0000' in visited:
			return -1
		
		while q:
			x, cnt = q.popleft()
			if x == target:
				return cnt
			
			for i in range(4):
				num = int(x[i])
				for k in [(num + 1) % 10, (num - 1) % 10]:
					t = x[:i] + str(k)	+ x[i + 1:]
					if t not in visited:
						visited.add(t)
						q.append((t, cnt + 1))
			
		return -1

a = Solution()

deadends = ["0201","0101","0102","1212","2002"]; target = "0202"
deadends = ["8888"]; target = "0009"
print(a.openLock(deadends, target))		
					
