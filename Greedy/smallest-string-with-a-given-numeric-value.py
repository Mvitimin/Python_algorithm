class Solution:
	def getSmallestString(self, n: int, k: int) -> str:
		res = ''
		for i in range(n):
			right = (n - i - 1) * 26
			if k > right:
				res += (chr(96 + k - right) + 'z' * (n - i - 1))
				break
			k -= 1
			res += 'a'		
		return res		
				
a = Solution()
n = 3; k = 27
#n = 5; k = 73
print(a.getSmallestString(n, k))				
				
