from typing import List
import collections

class Solution:
	def findOriginalArray(self, changed: List[int]) -> List[int]:
		
		if len(changed) % 2 != 0:
			return []
		
		map = collections.defaultdict(int)
		ans = []
		changed.sort()
		for num in changed:
			if num % 2 == 0 and map[num // 2] > 0:
				map[num // 2] -= 1
				ans.append(num // 2)
				continue
			map[num] += 1			
		return [] if len(ans) != (len(changed) // 2) else ans
		
a = Solution()
changed = [1,3,4,2,6,8]
#changed = [6,3,0,1]
#changed = [1]
changed = [0,0,0,0]
print(a.findOriginalArray(changed))	
		
				

