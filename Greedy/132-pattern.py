from typing import List

class Solution:
	def find132pattern(self, nums: List[int]) -> bool:
		n = len(nums)
		mins = []
		for i in range(n):
			if not mins or mins[-1] > nums[i]:
				mins.append(nums[i])
			else:
				mins.append(mins[-1])	
		stack = []
		for i in range(n - 1, -1, -1):
			#print(nums[i], mins, stack)
			if nums[i] > mins[-1]:
				if stack and stack[-1] < nums[i]:
					return True	
				stack.append(nums[i])
			mins.pop()
			while stack and mins and stack[-1] <= mins[-1]:
				stack.pop() 
		return False
		
				
a = Solution()
nums = [1, 2, 3, 4]
#nums = [3, 1, 4, 2]
#nums = [-1,3,2,0]
#nums = [1,0,1,-4,-3]
#nums = [3,5,0,3,4]
print(a.find132pattern(nums))
