from typing import List

class Solution:
	def maxProduct(self, nums: List[int]) -> int:
		
		po = ne = 1 
		ans = float('-inf')
		
		for i, num in enumerate(nums):
			po, ne = max(po * num, ne * num, num), min(ne * num, po * num, num)
			ans = max(ans, po)
		return ans	
		
a = Solution()
nums = [-2, -3, 0, -5, -6, 7, -2, -1]
#nums = [2,3,-2,4]
#nums = [-2,0,-1]
print(a.maxProduct(nums))			
