from typing import List
class Solution:
	def increasingTriplet(self, nums: List[int]) -> bool:
		a = b = float('inf')
		for n in nums:
			if n <= a:
				a = n 
			elif n <= b:
				b = n
			else:
				return True
		return True

a = Solution()
nums = [1, 2, 3, 4, 5]
#nums = [5,4,3,2,1]
#nums = [2,1,5,0,4,6]

#nums = [0,4,2,1,0,-1,-3]
#nums = [4, 4, 5, 5]
nums = [20,100,10,12,5,13]
print(a.increasingTriplet(nums))


