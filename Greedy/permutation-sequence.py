class Solution:
	def getPermutation(self, n: int, k: int) -> str:
		def factorial(n):
			if n == 1: return 1
			return n * factorial(n - 1)
		
		visited = set()
		res = 0
		x, y = n, factorial(n)				
		while x > 0:
			y = y // x
			for i in range(1, n + 1):
				if i not in visited:
					if y >= k:
						visited.add(i)
						res = (i + res * 10)
						break
					else: k -= y
			x -= 1				
		return str(res)		
			
a = Solution()		
'''	
for i in range(1, 25):
	print(a.getPermutation(4, i))
'''
n = 3; k = 3
n = 4; k = 9
n = 3; k = 1
print(a.getPermutation(n, k))			
