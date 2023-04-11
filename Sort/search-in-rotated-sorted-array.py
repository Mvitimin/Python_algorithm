from typing import List

class Solution:
	def search(self, nums: List[int], target: int) -> int:
		n = len(nums)
		i, j = 0, n - 1
		while i <= j:
			mid = i + (j - i) // 2
			if nums[mid] == target: return mid
			elif  nums[mid] >= nums[0] and nums[mid] >= nums[-1]:
				if nums[mid] > target:
					if target < nums[0]: i = mid + 1
					else: j = mid - 1
				else: i = mid + 1
			else:
				if nums[mid] < target:
					if target > nums[-1]: j = mid - 1
					else: i = mid + 1
				else: j = mid - 1
		return -1

a = Solution()
nums = [4,5,6,7,0,1,2]; target = 2	
#nums = [4,5,6,7,0,1,2]; target = 3	
#nums = [1]; target = 0
print(a.search(nums, target))
