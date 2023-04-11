from typing import List

class Solution:
	def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
		maps = {}
		stack = []
		for i, num in enumerate(nums2):
			while stack and stack[-1] < num:
				maps[stack.pop()] = num	
			stack.append(num)
		
		ans = []	
		for num in nums1:
			ans.append(maps.get(num, -1))
		return ans		
		
a = Solution()
nums1 = [4,1,2]; nums2 = [1,3,4,2]
nums1 = [2,4]; nums2 = [1,2,3,4]
print(a.nextGreaterElement(nums1, nums2))
