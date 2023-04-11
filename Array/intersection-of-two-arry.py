from typing import List
import collections

class Solution:
	def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
		ans = []
		counter = collections.Counter(nums2)
		for i in range(len(nums1)):
			if counter[nums1[i]]:
				counter[nums1[i]] -= 1
				ans.append(nums1[i])
		return ans
		

nums1 = [1,2,2,1]; nums2 = [2,2]
#nums1 = [4,9,5]; nums2 = [9,4,9,8,4]
a = Solution()
print(a.intersect(nums1, nums2))
