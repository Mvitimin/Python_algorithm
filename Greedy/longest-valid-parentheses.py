class Solution:
	def longestValidParentheses(self, s: str) -> int:
		n = len(s)
		ans = 0
		stack = [-1]
		for i, c in enumerate(s):
			if c == '(':
				stack.append(i)
			else:
				if stack[-1] != -1 and s[stack[-1]] == '(':
					stack.pop()
					ans = max(ans, i - stack[-1])	
				else:
					stack[-1] = i
		return ans
			
a = Solution()
s = "(()"
s = ")()())"
s = "()("
#s = ""
print(a.longestValidParentheses(s))		
	
