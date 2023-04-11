from typing import List

class Solution:
	def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
		
		slots1.sort()
		slots2.sort()
		
		m, n = len(slots1), len(slots2)
		
		i = j = 0
		while i < m and j < n:
			
			s1, e1 = slots1[i]
			s2, e2 = slots2[j]
			start, end = max(s1, s2), min(e1, e2)
			
			if end - start >= duration:
				return [start, start + duration]
			else:
				if e1 <= e2:
					i += 1
				else:
					j += 1
		return []
		
a = Solution()
slots1 = [[10,50],[60,120],[140,210]]; slots2 = [[0,15],[60,70]]; duration = 8
#slots1 = [[10,50],[60,120],[140,210]]; slots2 = [[0,15],[60,70]]; duration = 12
print(a.minAvailableDuration(slots1, slots2, duration))
				
					
		
		
		
