class Solution:
	def kthGrammar(self, n: int, k: int) -> int:
		if n == 1:
			return 0
		p = 2 ** (n - 2)
		if k <= p:
			return self.kthGrammar(n - 1, k)
		return 1 - self.kthGrammar(n - 1, k - p)
			
a = Solution()
print(a.kthGrammar(4, 6))
