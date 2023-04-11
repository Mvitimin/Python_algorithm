class Solution:
	def smallestFactorization(self, num: int) -> int:
		even = [8, 6, 4, 2]
		odd = [9, 7, 5, 3]
		if num == 1: return 1		
		ans, mul = 0, 1
		while num != 1:	
			for i in range(4):
				if num % even[i] == 0:
					ans += even[i] * mul 
					num = num // even[i]
					mul *= 10
					break
				elif num % odd[i] == 0:
					ans += odd[i] * mul
					num = num // odd[i]
					mul *= 10
					break
			else: return 0
	
		return ans if ans <= (2 ** 31 - 1) else 0
	
a = Solution()
num = 48
#num = 18000000
print(a.smallestFactorization(num))
x = 2147483647
y = 2 ** 31 - 1
print(x == y)
