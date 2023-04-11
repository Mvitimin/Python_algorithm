from typing import List

class Solution:
	def movesToMakeZigzag(self, nums: List[int]) -> int:
		n = len(nums)
		if n <= 1: return 0
		even_moves = odd_moves = 0
		for i in range(n):
			if i == 0: m = nums[i + 1]
			elif i == n - 1: m = nums[i - 1]
			else: m = min(nums[i + 1], nums[i - 1])
	
			if i % 2 == 1 and m <= nums[i]:
				even_moves += (nums[i] - m + 1)
			if i % 2 == 0 and m <= nums[i]: 
				odd_moves += (nums[i] - m + 1)		
		return min(even_moves, odd_moves)
		
		
a = Solution()
nums = [9, 6, 1, 6, 2]
#nums = [1, 2, 3]
#nums = [10,4,4,10,10,6,2,3]
print(a.movesToMakeZigzag(nums))
