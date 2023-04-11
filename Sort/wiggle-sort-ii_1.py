from typing import List

class Solution:	
	def wiggleSort(self, nums: List[int]) -> None:
		nums.sort(reverse=True)
		mid = int(len(nums) / 2)
		nums[::2], nums[1::2] = nums[mid:], nums[:mid]
		
		print(nums)
	
a = Solution()
nums = [1,5,1,1,6,4]
nums = [1, 5, 2, 2, 1, 4]
nums = [1,3,2,2,3,1]
nums = [1,5,1,1,6,4]
#nums = [5,3,1,2,6,7,8,5,5]
a.wiggleSort(nums)




