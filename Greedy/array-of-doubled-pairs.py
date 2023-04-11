from typing import List
import collections

class Solution:
	def canReorderDoubled(self, arr: List[int]) -> bool:
		arr.sort(key=lambda x: abs(x))
		counts = collections.Counter(arr)
		n = len(arr)
		pairs = 0
		for i in range(n):
			if counts[arr[i]] > 0:
				counts[arr[i]] -= 1
				if counts[2 * arr[i]] > 0:
					counts[arr[i] * 2] -= 1
					pairs += 1		
				else: return False
		return True
	
a = Solution()
arr = [3,1,3,6]
arr = [2,1,2,6]
arr = [4,-2,2,-4]
arr = [1,2,4,16,8,4]
arr = [2,4,0,0,8,1]
arr = [-33, 0]
print(a.canReorderDoubled(arr))
