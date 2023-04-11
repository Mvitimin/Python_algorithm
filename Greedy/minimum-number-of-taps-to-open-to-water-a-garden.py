from typing import List

class Solution:
	def minTaps(self, n: int, ranges: List[int]) -> int:
		event = []
		for i, r in enumerate(ranges):
			event.append((max(i - r, 0), i + r))
		event.sort(reverse=True)
		ans = end = 0
		
		while event:	
			p = end 
			while event and event[-1][0] <= end:
				s, e = event.pop()
				p = max(e, p)
			if p == end: return -1
			ans += 1
			end = p
			if end >= n: return ans
		return -1		
				
		
a = Solution()
n = 5; ranges = [3,4,1,1,0,0]	
n = 3; ranges = [0,0,0,0]
n = 8; ranges = [4,0,0,0,4,0,0,0,4]
n = 9; ranges = [0,5,0,3,3,3,1,4,0,4]
print(a.minTaps(n, ranges))
