from typing import List

class Solution:
	def maxSatisfaction(self, satisfaction: List[int]) -> int:
		satisfaction.sort()
		ans = total = 0
		while satisfaction and satisfaction[-1] + total >= 0:
			total += satisfaction.pop()
			ans += total
		return ans
			
		
			
satisfaction = [-1,-8,0,5,-9]
satisfaction = [4,3,2]
#satisfaction = [-1,-4,-5]
a = Solution()
print(a.maxSatisfaction(satisfaction))
