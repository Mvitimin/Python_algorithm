from typing import List
class Solution:
	def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
		n = len(nums)
		i = 0
		for i in range(n):
			idx = abs(nums[i]) - 1
			if nums[idx] > 0:
				nums[idx] *= -1	
		
		ans = []
		for i in range(n):
			if nums[i] > 0:
				ans.append(i + 1)		
		return ans

a = Solution()
nums = [4,3,2,7,8,2,3,1]
nums = [2, 3, 4, 1,1, 2, 5]
print(a.findDisappearedNumbers(nums))		
					
			

