from typing import List
import collections

class Solution:
	def longestSubsequence(self, arr: List[int], difference: int) -> int:
		
		maps = collections.defaultdict(int)
		ans = 0
		for i, num in enumerate(arr):
			maps[num] = maps[num - difference] + 1
			ans = max(ans, maps[num])
		return ans

a = Solution()
arr = [1,2,3,4]; difference = 1
arr = [1,3,5,7]; difference = 1
arr = [1,5,7,8,5,3,4,2,1]; difference = -2
print(a.longestSubsequence(arr, difference))
		
