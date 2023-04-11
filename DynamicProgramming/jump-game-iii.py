from typing import List
import collections
class Solution:
	def canReach(self, arr: List[int], start: int) -> bool:
		n = len(arr)
		for i in range(n):
			if arr[i] == 0:
				break
		else:
			return False
			
		q = collections.deque([start])
		visited = collections.defaultdict(int)
		while q:
			index = q.popleft()
			if arr[index] == 0:
				return True
			for x in [index + arr[index], index - arr[index]]:
				if 0 <= x < n and visited[x] == 0:
					q.append(x)
					visited[x] = 1
		return False	
		
a = Solution()
arr = [4,2,3,0,3,1,2]; start = 5
arr = [4,2,3,0,3,1,2]; start = 0
arr = [3,0,2,1,2]; start = 2
print(a.canReach(arr, start))

