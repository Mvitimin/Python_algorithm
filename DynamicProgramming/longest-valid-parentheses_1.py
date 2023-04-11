from functools import lru_cache

class Solution:
	def longestValidParentheses(self, s: str) -> int:
		n = len(s)
		stack = []
		prev, ans = -1, 0
		for i, k in enumerate(s):
			if k == '(':
				stack.append(i)
			else:
				if stack: 
					stack.pop()
					ans = max(ans, i - (stack[-1] if stack else prev))
				else:
					prev = i
		return ans

a = Solution()
s = '(()'
#s = ")()())"
#s = ""
#s = "()(()"
print(a.longestValidParentheses(s))				
