from typing import List

class Solution:
	def shipWithinDays(self, weights: List[int], days: int) -> int:
		i, j = max(weights), sum(weights)
		
		while i <= j:
			
			mid = i + (j - i) // 2
			k = m = 0
			for w in weights:
				if k + w <= mid:
					k += w
				else:
					k = w
					m += 1
			
			if m + 1 <= days:
				j = mid - 1
			else:
				i = mid + 1
		return i
				
		

weights = [1,2,3,4,5,6,7,8,9,10]; days = 5
#weights = [3,2,2,4,1,4]; days = 3
#weights = [1,2,3,1,1]; days = 4
a = Solution()
print(a.shipWithinDays(weights, days))		
		
