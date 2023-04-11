class Solution:
	def removeKdigits(self, num: str, k: int) -> str:
		stack = []
		n = len(num)
		
		for ch in num:
			while k and stack and stack[-1] > ch:
				stack.pop()
				k -= 1
			stack.append(ch)
		ans = ''.join(stack[:len(stack) - k])
		return str(int(ans)) if ans else '0'

a = Solution()
num = "1432219"; k = 3
num = "1173"; k = 2
num ="1234567890"; k = 9
#num = "10200"; k = 1
#num = "10"; k = 2
print(a.removeKdigits(num, k))				
