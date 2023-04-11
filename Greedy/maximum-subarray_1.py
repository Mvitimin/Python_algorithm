from typing import List

class Solution:
	def maxSubArray(self, nums: List[int]) -> int:
		
		def find(nums, left, right):
			if left > right:
				return float('-inf')
			
			mid = left + (right - left) // 2
			curr = leftT = rightT = 0
			
			for i in range(mid - 1, left - 1, -1):
				curr += nums[i]
				leftT = max(leftT, curr)
			
			curr = 0
			
			for i in range(mid + 1, right + 1):
				curr += nums[i]
				rightT = max(rightT, curr)

			res = leftT + nums[mid] + rightT
			
			halfL, halfR = find(nums, left, mid - 1), find(nums, mid + 1, right)
			return max(res, halfR, halfL)		
		return find(nums, 0, len(nums) - 1)		
		
a = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
#nums = [1]
#nums = [5,4,-1,7,8]
#nums = [-1]
print(a.maxSubArray(nums))

