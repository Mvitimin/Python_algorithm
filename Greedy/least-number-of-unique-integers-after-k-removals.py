from typing import List
import collections

class Solution:
	def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
		counter = collections.Counter(arr)
		keys = list(counter.keys())
		keys.sort(key=lambda x : counter[x])
		n = len(keys)
		for i, key in enumerate(keys):
			if k >= counter[key]:
				k -= counter[key]
			else:
				return n - i
		return 0
			
a = Solution()
arr = [5,5,4]; k = 1
arr = [4,3,1,1,3,3,2]; k = 3
arr = [1, 2, 3]; k = 3
print(a.findLeastNumOfUniqueInts(arr, k))
