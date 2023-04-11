import re
import collections
class Solution:
	def countOfAtoms(self, formula: str) -> str:
		parse = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", formula)
		stack = [collections.Counter()]
		for name, m1, left_open, right_open, m2 in parse:
			if name:
				stack[-1][name] += int(m1 or 1)
			if left_open:
				stack.append(collections.Counter())
			if right_open:
				top = stack.pop()
				for k in top:
					stack[-1][k] += top[k] * int(m2 or 1)
		return ''.join([name + (str(stack[-1][name]) if stack[-1][name] > 1 else '') for name in sorted(stack[-1])])
			
			
a = Solution()
formula = "K4(ON(SO3)2)2"
formula = "Mg(OH)2"
formula = "H2O"
print(a.countOfAtoms(formula))		
		
