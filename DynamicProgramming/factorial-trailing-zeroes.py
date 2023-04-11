class Solution:
	def trailingZeroes(self, n: int) -> int:
		x = 0
		while n > 0:
			n = n // 5
			x += n
			
		return x

a = Solution()
k = 1
n = 30
#n = 12
for i in range(1, n + 1):
	k *= i
print(k)
print(a.trailingZeroes(n))

