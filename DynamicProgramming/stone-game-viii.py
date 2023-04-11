from typing import List
from itertools import accumulate
class Solution:
	def stoneGameVIII(self, stones: List[int]) -> int:
		s = list(accumulate(stones))[1:]
		max_val = s[-1]
		ans = float('-inf')
		for i in range(len(s) - 2, -1, -1):
			ans = s[i] - max_val
			max_val = max(max_val, ans)
		return max_val
			
a = Solution()
stones = [-1,2,-3,4,-5]
#stones = [-10,-12]
#stones = [7,-6,5,10,5,-2,-6]
print(a.stoneGameVIII(stones))
