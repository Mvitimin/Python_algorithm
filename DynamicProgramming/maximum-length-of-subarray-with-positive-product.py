from typing import List

class Solution:
	def getMaxLen(self, nums: List[int]) -> int:
		pos = neg = 0
		ans = 0
		for n in nums:
			if n < 0:
				neg, pos = pos + 1, (neg + 1) if neg != 0 else 0 
			elif n > 0:
				neg, pos = (neg + 1) if neg != 0 else 0, pos + 1
			else: pos = 0; neg = 0
			ans = max(pos, ans)	
		return ans

a = Solution()
nums = [1, -5, -4, 1, 2, -3]
nums = [1, 7, -2, -3, 0, 1, 6]
nums = [-1, 1, 2, -3, 4, 5]
nums = [1,-2,-3,4]
nums = [0,1,-2,-3,-4]
nums = [-1,-2,-3,0,1]
print(a.getMaxLen(nums))			
				
			
		

