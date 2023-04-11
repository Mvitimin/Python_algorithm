
# minimum-deletion-cost-to-avoid-repeating-letters/

from typing import List

class Solution:
	def minCost(self, s: str, cost: List[int]) -> int:
		stack = []
		for i, char in enumerate(s):
			if stack and char == s[stack[-1]]:
				if cost[stack[-1]] < cost[i]:
					stack.pop()
					stack.append(i)
			else:
				stack.append(i)
		res = sum([cost[i] for i in stack])
		return sum(cost) - res
		

a = Solution()
#s = "aabaa"
#cost = [1,2,3,4,1]
#s = "abaac"
#cost = [1,2,3,4,5]
#s = "aaaaabcbbb"
#cost = [1,1,3,1,1,2,3,6,7,8]
s = "aaabbbabbbb"
cost = [3,5,10,7,5,3,5,5,4,8,1]
#s = "a"
#cost = [5]
print(a.minCost(s, cost))
