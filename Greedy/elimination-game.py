class Solution:
	def lastRemaining(self, n: int) -> int:
		def dp(n, direction):
			if n == 1:
				return 1
			if direction == 0:
				return 2 * dp(n // 2, 1)
			return 2 * dp(n // 2, 0) + n % 2 - 1	
		return dp(n, 0)
				
a = Solution()
n = 9
print(a.lastRemaining(n))
