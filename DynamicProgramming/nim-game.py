class Solution:
	def canWinNim(self, n: int) -> bool:
		return n % 4 != 0 
		
a = Solution()
print(a.canWinNim(8))
