from functools import lru_cache
class Solution:
	def numberOfWays(self, numPeople: int) -> int:
	
		@lru_cache(None)
		def dp(people):
			if people <= 2:
				return 1
				
			mid = people // 2	
			val = 0
			for i in range(2, mid + 1, 2):
				val += (dp(i - 2) * dp(people - i)) * 2
			return (val + (dp(mid - 1) * dp(people - mid - 1) if mid % 2 == 1 else 0)) % (10 ** 9 + 7)
		return dp(numPeople)

a = Solution()
print(a.numberOfWays(140))

