from typing import List

class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		n = len(nums)
		ans = []
		p = 1
		for i in range(n):
			ans.append(p)
			p *= nums[i]
		
		p = 1
		for i in range(n - 1, -1, -1):
			ans[i] = ans[i] * p
			p *= nums[i]
		
		return ans

	
a = Solution()
nums = [1, 2, 3, 4]
nums = [-1,1,0,-3,3]
print(a.productExceptSelf(nums))	
		
			
			

