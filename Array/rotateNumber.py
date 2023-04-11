class Solution:
	def rotatedDigits(self, n: int) -> int:
		s = str(n)
		digits = {'0': 0, '1': 0, '8': 0, '6': 1, '9': 1, '2': 1, '5': 1}
		
		def check(k, same):
			return 1 if same and k and int(k) <= n and k[0] != '0' else 0		
			
		def solve(k, same):
			if len(k) > len(s):
				return 0	
			val = check(k, same)
			for d in digits:
				val += solve(k + d, same + digits[d])	
			return val		
		
		return solve('', 0)
		
		
			
a = Solution()
n = 2
print(a.rotatedDigits(n))			
			
