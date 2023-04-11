from typing import List

class Solution:
	def calPoints(self, ops: List[str]) -> int:
		ans = []
		for op in ops:
			if op == 'C':
				ans.pop()
			elif op == 'D':
				ans.append(ans[-1] * 2)
			elif op == '+':
				ans.append(ans[-1] + ans[-2])
			else:
				ans.append(int(op))
		return sum(ans)
		
a = Solution()
ops = ["5","2","C","D","+"]
ops = ["5","-2","4","C","D","9","+","+"]
ops = ["1"]
print(a.calPoints(ops))

