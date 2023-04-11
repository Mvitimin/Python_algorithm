
from typing import List
from functools import cmp_to_key
class Solution:
	def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
		def compare(a, b):
			if abs(a - x) == abs(b - x):
				return 1 if a > b else -1
			else:
				return 1 if abs(a - x) > abs(b - x) else -1
		arr.sort(key=cmp_to_key(compare))
		return sorted(arr[:k])

a = Solution()
arr = [1, 2, 3, 4, 5]; k = 4; x = 3
arr = [1,2,3,4,5]; k = 4; x = -1
arr = [1,1,1,10,10,10]; k = 1; x = 9
print(a.findClosestElements(arr, k, x))
