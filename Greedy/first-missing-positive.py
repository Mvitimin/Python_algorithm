from typing import List

class Solution:
	def firstMissingPositive(self, nums: List[int]) -> int:
		nums_set = set()
		for num in nums:
			if num > 0:
				nums_set.add(num)	
		i = 1
		while i in nums_set:
			i += 1
		return i 

a = Solution()		
nums = [3,4,-1,1]
nums = [7,8,9,11,12]
nums = [1,2,0]
print(a.firstMissingPositive(nums))

