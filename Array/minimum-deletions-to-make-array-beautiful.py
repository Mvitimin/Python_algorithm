from typing import List

class Solution:
	def minDeletion(self, nums: List[int]) -> int:
		n = len(nums) 	
		stack = []
		for i in range(n):
			if len(stack) % 2 == 0:
				stack.append(nums[i])
			else:
				if stack[-1] == nums[i]:
					stack.pop()
				stack.append(nums[i])
																
		return n - len(stack) + len(stack) % 2

a = Solution()
nums = [1,1,2,3,5]
nums = [1,1,2,2,3,3]
print(a.minDeletion(nums))
