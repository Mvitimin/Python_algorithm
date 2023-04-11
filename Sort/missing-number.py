from typing import List

class Solution:
	def missingNumber(self, nums: List[int]) -> int:
		n = len(nums)
		s = n * (n + 1) // 2
		for num in nums:
			s -= num
		return s
			
				
						
a = Solution()
nums = [3,0,1]
#nums = [0, 1]
#nums = [9,6,4,2,3,5,7,0,1]
#nums = [0]
#nums = [1]
print(a.missingNumber(nums))	
				
			
print(2 ^ 3 ^ 3)
