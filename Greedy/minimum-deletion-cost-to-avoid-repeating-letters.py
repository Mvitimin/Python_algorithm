
# minimum-deletion-cost-to-avoid-repeating-letters/

from typing import List

class Solution:
	def minCost(self, s: str, cost: List[int]) -> int:
		
		prev = ans = 0
		max_c = -1
		
		for i in range(1, len(s)):
			if s[i] == s[prev]:
				max_c = max(max(cost[prev], cost[i]), max_c)
				ans += cost[prev]
				if (i != len(s) -1 and s[i] != s[i + 1]) or i == len(s) - 1:
					ans += (cost[i] - max_c)
			else:
				max_c = -1
			prev = i
		return ans


a = Solution()
#s = "aabaa"
#cost = [1,2,3,4,1]
#s = "abaac"
#cost = [1,2,3,4,5]
#s = "aaaaabcbbb"
#cost = [1,1,3,1,1,2,3,6,7,8]
#s = "aaabbbabbbb"
#cost = [3,5,10,7,5,3,5,5,4,8,1]
s = "a"
cost = [5]
print(a.minCost(s, cost))
