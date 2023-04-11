class Solution:
	def hammingWeight(self, n: int) -> int:
		ans = 0
		while n:
			ans += n & 1
			n = n >> 1
		return ans
		
n = 0b00000000000000000000000000001011
n = 0b00000000000000000000000010000000
n = 0b11111111111111111111111111111101
a = Solution()
print(a.hammingWeight(n))
