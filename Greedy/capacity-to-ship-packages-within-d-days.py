from typing import List

class Solution:
	def shipWithinDays(self, weights: List[int], days: int) -> int:
		l, r = max(weights), sum(weights)
		while l <= r:
			mid = l + (r - l) // 2
			cur = cnt = 0
			for w in weights:
				cur += w
				if cur > mid:
					cur = w 
					cnt += 1
			if cnt + 1 > days:
				l = mid + 1
			else:
				r = mid - 1
		return l 
			
				
a = Solution()
weights = [1,2,3,4,5,6,7,8,9,10]; days = 5
weights = [3,2,2,4,1,4]; days = 3
weights = [1,2,3,1,1]; days = 4
print(a.shipWithinDays(weights, days))	
