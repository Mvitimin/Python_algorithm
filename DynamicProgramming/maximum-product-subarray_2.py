from typing import List

class Solution:
	def maxProduct(self, nums: List[int]) -> int:
		ans = float('-inf')
		po = ne = 1
		
		for num in nums:
			po, ne = max(num, po * num, ne * num), min(num, ne * num, po * num)	
			ans = max(ans, po)	
		return ans
		
a = Solution()
nums = [2,3,-2,4]
#nums = [-2,0,-1]
#nums = [0, 2]
#nums = [-3,0,1,-2]
#nums = [-2,3,-4]
print(a.maxProduct(nums))

