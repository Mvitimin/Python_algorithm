
class Solution:
	def removeKdigits(self, num: str, k: int) -> str:
		stack = []
		for digit in num:
			while k and stack and stack[-1] > digit:
				stack.pop()
				k -= 1
			stack.append(digit)
		nums = stack[:-k] if k > 0 else stack[:]
		return ''.join(nums).lstrip('0') or '0'

a = Solution()
num = "1432219"; k = 3
#num = "1235520"; k = 3
#num = "10200"; k = 1
num = "10"; k = 2
#num = "112"; k = 1
print(a.removeKdigits(num, k))
