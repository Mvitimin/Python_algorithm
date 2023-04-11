from typing import List

class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		n, m = len(nums1), len(nums2)
		mid = (n + m) // 2
		i = j = 0
		index = tmp = 0
		ans = [0, 0]
		while i < n or j < m and index <= mid:
			if i < n and j < m:
				if nums1[i] <= nums2[j]: 
					tmp = nums1[i]; i += 1
				else: tmp = nums2[j]; j += 1 
			elif i < n:
				tmp = nums1[i]; i += 1
			else:
				tmp = nums2[j]; j += 1
			if index in [mid, mid - 1]: 
				ans[index - mid + 1] = tmp  
			index += 1	
		return sum(ans) / 2 if (n + m) % 2 == 0 else ans[1]	

a = Solution()
nums1 = [1,2]; nums2 = [3,4]
nums1 = [1, 5, 8]; nums2 = [2, 6, 9]
nums1 = [1, 2, 6]; nums2 = [3, 7]
nums1 = []; nums2 = [1]
print(a.findMedianSortedArrays(nums1, nums2))

