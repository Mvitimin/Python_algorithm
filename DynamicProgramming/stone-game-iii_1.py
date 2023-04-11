from typing import List
from functools import lru_cache
class Solution:
	def stoneGameIII(self, stoneValue: List[int]) -> str:
		n = len(stoneValue)
		
		@lru_cache(None)
		def dp(i):
			if i >= n:
				return 0
			max_val = float('-inf')
			for j in range(3):
				next = j + i + 1
				max_val = max(max_val, sum(stoneValue[i:next]) - dp(next))
			return max_val
			
		ans = dp(0)
		if ans < 0:
			return 'Bob'
		elif ans > 0:
			return 'Alice'	
		else:
			return 'Tie'
		
	
a = Solution()
stoneValue = [0, 1, 2, -3, -4, 5, -6]
values = [1, 2, 3, 7]
#values = [1, 2, 3, -9]
#values = [1,2,3,6]
#values = [1,2,3,-1,-2,-3,7]
#values = [-1,-2,-3]
print(a.stoneGameIII(values))
				
				
