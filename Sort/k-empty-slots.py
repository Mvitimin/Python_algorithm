from typing import List
import heapq

class Solution:
	def kEmptySlots(self, bulbs: List[int], k: int) -> int:
		n = len(bulbs)
		if k > n:
			return -1
		map = [float('inf')] * (n + 1)
		for day, b in enumerate(bulbs, 1):
			map[b] = day
		
		ans = float('inf')
		
		l, r = 1, k + 2
		for bulb in range(1, n + 1):
			if r > n:
				break
			val = max(map[l], map[r])
			if map[bulb] > val:
				continue
			if bulb == r:
				ans = min(ans, val)
			
			l, r = bulb, bulb + k + 1
			
					
		return ans if ans != float('inf') else -1
			
		

a = Solution()
bulbs = [1,3,2]; k = 1
#bulbs = [1,3,2]; k = 0
#bulbs = [6,5,8,9,7,1,10,2,3,4]; k = 2
#bulbs = [1,2,3]; k = 1		
#bulbs = [3,9,2,8,1,6,10,5,4,7]; k = 1
print(a.kEmptySlots(bulbs, k))
				
				
						
			
			
		

