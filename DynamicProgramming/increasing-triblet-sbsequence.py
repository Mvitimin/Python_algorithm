from typing import List

class Solution:
	def increasingTriplet(self, nums: List[int]) -> bool:
		
		a = b = float('inf')
		for n in nums:
			if a >= n:
				a = n
			elif b >= n:
				b = n
			else:
				return True
												
		return False


a = Solution()
nums = [1, 2, 3, 4, 5]
#nums = [5,4,3,2,1]
#nums = [2,1,5,0,4,6]		
nums = [1, 7, 3, 4]		
mums = [4, 2, 3, 2, 1, 8]
nums = [20,100,10,12,5,13]
nums = [1, 5, 3, 4]
print(a.increasingTriplet(nums))
			
