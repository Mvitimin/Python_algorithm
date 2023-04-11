from typing import List
class Solution:
	def canPartition(self, nums: List[int]) -> bool:
		t = sum(nums)
		n = len(nums)
	
		if t == 0:
			return n >= 2
		
		if t % 2 == 1:
			return False
		
		sums = set([0])
		
		for i in range(n):
			tmp = set([k for k in sums])
			for k in sums:
				if k + nums[i] == t // 2:
						return True	
				if k + nums[i] < t // 2:
					tmp.add(k + nums[i])
			sums = tmp
		return False	
			
				
				
		
		
		
a = Solution()
nums = [1, 5, 11, 5]
#nums = [1, 2, 3, 5]
print(a.canPartition(nums))

	
			
