

from typing import List
class Solution:
	def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
		slots1.sort(key=lambda x: x[0])
		slots2.sort(key=lambda x: x[0])
		p1 = p2 = 0
		while p1 < len(slots1) and p2 < len(slots2):
			if slots1[p1][1] <= slots2[p2][0]:
				p1 += 1
			elif slots2[p2][1] <= slots1[p1][0]:
				p2 += 1
			else:
				start, end = max(slots1[p1][0], slots2[p2][0]), min(slots1[p1][1], slots2[p2][1])
				if (end - start) >= duration:
					return [start, start + duration]				
				if slots1[p1][0] < slots2[p2][0]:
					p1 += 1
				else:
					p2 += 1 
				
		return []		

				
slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration = 8

'''
slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration = 12
'''
a = Solution()
print(a.minAvailableDuration(slots1, slots2, duration))
