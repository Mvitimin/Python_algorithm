from functools import lru_cache

class Solution:
	def getKth(self, lo: int, hi: int, k: int) -> int:
		
		@lru_cache(None)
		def findSteps(x):
			if x == 1:
				return 0
			x = x // 2 if x % 2 == 0 else 3 * x + 1
			return findSteps(x) + 1
		
		
		arr = [i for i in range(lo, hi + 1)]		
		arr.sort(key=lambda x: (findSteps(x), x))
		return arr[k - 1]
		
a = Solution()
lo = 12; hi = 15; k = 2
lo = 7; hi = 11; k = 4
print(a.getKth(lo, hi, k))
