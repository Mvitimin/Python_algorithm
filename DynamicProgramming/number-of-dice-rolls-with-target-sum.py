from functools import lru_cache

class Solution:
	def numRollsToTarget(self, d: int, f: int, target: int) -> int:
		modulo = 10 ** 9 + 7
		@lru_cache(None)
		def helper(n, total, faces):
			if n <= 0:
				if total == 0:
					return 1
				return 0	
			ways = 0	
			for i in range(1, min(faces, total) + 1):
				if total - i >= 0:
					ways += helper(n - 1, total - i, faces)
			return ways	% modulo
		return helper(d, target, f)

a = Solution()
d = 1; f = 6; target = 3
d = 2; f = 6; target = 7
d = 2; f = 5; target = 10
d = 1; f = 2; target = 3
d = 30; f = 30; target = 500
print(a.numRollsToTarget(d, f, target))
