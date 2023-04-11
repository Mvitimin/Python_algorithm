from typing import List
from functools import lru_cache
class Solution:
	def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
		counts = {}
		dp = {}
		for i, s in enumerate(strs):
			ans = 0
			for c in s:
				if c == '0': ans += 1
			counts[i] = (ans, len(s) - ans) 
		
		@lru_cache(None)		
		def helper(i, cur_zeros, cur_ones):
			if cur_zeros == cur_ones == 0 or i >= len(strs):
				return 0
			not_selected = helper(i + 1, cur_zeros, cur_ones)
			zeros, ones = counts[i]
			if cur_zeros - zeros >= 0 and cur_ones - ones >= 0:
				selected = max(not_selected, 1 + helper(i + 1, cur_zeros - zeros, cur_ones - ones))
				return selected
			return not_selected
		return helper(0, m, n)
		
		

a = Solution()
strs = ["10","0001","111001","1","0"]; m = 5; n = 3
#strs = ["10","0","1"]; m = 1; n = 1
#strs = ["10","0001","111001","1","0"]; m = 4; n= 3
#strs = ["10","0001","111001","1","0"]; m = 50; n = 50
result = a.findMaxForm(strs, m, n)
print(result)
