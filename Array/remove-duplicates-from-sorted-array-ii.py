from typing import List

class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		n = len(nums)
		start = 0
		cnt = 0
		
		for i, num in enumerate(nums):
			if num == nums[start]:
				nums[start + cnt] = num
				cnt += 1		
			else:
				end = start + min(cnt, 2)
				nums[end] = num 
				start, cnt = end, 1
		
		return start + min(cnt, 2) 
a = Solution()
nums = [1, 1, 1, 2, 2, 3]
nums = [0,0,1,1,1,1,2,3,3]
nums = [0,1,1,2,2,2,3,4,5,5,5]
print(a.removeDuplicates(nums))		

