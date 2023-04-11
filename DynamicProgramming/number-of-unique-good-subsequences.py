class Solution:
	def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
		n = len(binary)
		endZero = endOne = 0
		hasZero = False
		
		for i, c in enumerate(binary):
			if c == '0':
				endZero = endZero + endOne
				hasZero = True
			else:
				endOne = endZero + endOne + 1
		return (endZero + endOne + hasZero) % (10 ** 9 + 7)
			
		
		
a = Solution()
binary = "101"
binary = "11"
ans = a.numberOfUniqueGoodSubsequences(binary)
print(ans)
