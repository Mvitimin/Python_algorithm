from typing import List
from functools import lru_cache
class Solution:
	def stoneGameV(self, stoneValue: List[int]) -> int:
		@lru_cache(None)
		def dp(start, end, total):	
			if end - start <= 1:
				return 0
			
			left = 0
			max_val = val = 0
			for i in range(start + 1, end):
				left += stoneValue[i - 1]
				right = total - left
				if left > right:
					val = right + dp(i, end, right)
				elif right > left:
					val = left + dp(start, i, left)
				else:
					val = max(right + dp(i, end, right), left + dp(start, i, left))
				max_val = max(val, max_val)
			return max_val
		return dp(0, len(stoneValue), sum(stoneValue))

a = Solution()
stoneValue = [6,2,3,4,5,5]
#stoneValue = [7,7,7,7,7,7,7]
#stoneValue = [4]
#stoneValue = [10,9,8,7,6,5,4,3,2,1]
stoneValue = [68,75,25,50,34,29,77,1,2,69]
print(a.stoneGameV(stoneValue))
			
																								
