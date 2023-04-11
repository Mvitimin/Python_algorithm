from typing import List

class Solution:
	def wiggleMaxLength(self, nums: List[int]) -> int:
		n = len(nums)
		if n <= 1:
			return n
		prev = nums[1] - nums[0]
		ans = 2 if prev != 0 else 1
		for i in range(1, n - 1):
			diff = nums[i + 1] - nums[i]
			if (diff > 0 and prev <= 0) or (diff < 0 and prev >=0):
				ans += 1
				prev = diff
		return ans 	
			
			
			
					
nums = [1,7,4,9,2,5]
nums = [1,17,5,10,13,15,10,5,16,8]
nums = [1,2,3,4,5,6,7,8,9]
nums = [0, 0, 0]
nums = [3,3,3,2,5]
a = Solution()
print(a.wiggleMaxLength(nums))
