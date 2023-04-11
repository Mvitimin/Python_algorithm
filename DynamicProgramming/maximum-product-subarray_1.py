from typing import List

class Solution:
	def maxProduct(self, nums: List[int]) -> int:
		n = len(nums)
		po = ne = ans = nums[0]	
		for i in range(1, n):		
			po, ne = max(nums[i], po * nums[i], ne * nums[i]), min(nums[i], po * nums[i], ne * nums[i])
			ans = max(ans, po)			
		return ans
		
a = Solution()
nums = [2,3,-2,4]
nums = [-2, 0, -1]
nums = [-2, 3, -4]
print(a.maxProduct(nums))
	
			
