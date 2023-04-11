class Solution:
	def minAddToMakeValid(self, s: str) -> int:
		stack = []
		moves = 0
		for c in s:
			if c == '(':
				stack.append(c)
			else:
				if not stack: moves += 1
				else: stack.pop()
		moves += len(stack)
		return moves

a = Solution()
s = "())"
s = "((("
s = "()"
s = "()))(("
print(a.minAddToMakeValid(s))		
			
