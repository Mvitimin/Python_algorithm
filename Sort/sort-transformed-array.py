from typing import List
import collections
class Solution:
	def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
		ans = collections.deque([])
		i, j = 0, len(nums) - 1 
		
		def f(v):
			return a * v * v + b * v + c
		
		if a == 0:
			if b >= 0: return [f(num) for num in nums]
			else: return [f(nums[i]) for i in range(j, -1, -1)] 	
		
		comp = -b / (2 * a)
		
		while i <= j:
			if abs(nums[i] - comp) >= abs(nums[j] - comp):
				if a > 0: ans.appendleft(f(nums[i]))
				else: ans.append(f(nums[i]))
				i += 1
			else: 
				if a > 0: ans.appendleft(f(nums[j])) 
				else: ans.append(f(nums[j]))
				j -= 1
		return ans 
				
						
			
			
		

#nums = [-4,-2,2,4]; a = 0; b = 3; c = 5
nums = [-4,-2,2,4]; a = 0; b = -3; c = 5
t = Solution()
print(t.sortTransformedArray(nums, a, b, c))

