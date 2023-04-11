from typing import List

class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		n = len(nums)
		
		def solve(l, r):
			if l == r:
				return nums[l]
			
			mid = l + (r - l) // 2
			
			left = solve(l, mid)
			right = solve(mid + 1, r)
			
			c1 = sum(1 for i in range(n) if nums[i] == left)
			c2 = sum(1 for i in range(n) if nums[i] == right)
			return left if c1 > c2 else right
			
		return solve(0, n - 1)		
								
								
a = Solution()
nums = [2, 2, 1]
nums = [3, 2, 3]
nums = [2,2,1,1,1,2,2]
nums = [6, 5, 5]
#nums = [1,3,1,1,4,1,1,5,1,1,6,2,2]
print(a.majorityElement(nums))			
		
