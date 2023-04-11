from typing import List
import collections

class Solution:
	def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
		n = len(nums1)
		
		sums = collections.defaultdict(int)
		for i in range(n):
			for j in range(n):
				sums[nums1[i] + nums2[j]] += 1
		
		ans = 0
		for i in range(n):
			for j in range(n):		
				k = nums3[i] + nums4[j]
				if -k in sums:
					ans += sums[-k]
		return ans
		
		
nums1 = [1,2]; nums2 = [-2,-1]; nums3 = [-1,2]; nums4 = [0,2]
nums1 = [0]; nums2 = [0]; nums3 = [0]; nums4 = [0]
a = Solution()
print(a.fourSumCount(nums1, nums2, nums3, nums4))
			
				
