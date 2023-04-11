from typing import List
import collections
class Solution:
	def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
		events = []
		ans = [0] * len(nums2)
		for i, n in enumerate(nums2):
			events.append((n, i)) 
		events.sort()
		q = collections.deque(events)
		nums1.sort()
		for i in range(len(nums1) - 1, -1, -1):
			n2, index = q.pop()
			if nums1[-1] > n2:
				ans[index] = nums1[-1]
				nums1.pop()
			else:
				q.appendleft((n2, index))
		for n2, index in q:
			ans[index] = nums1.pop()		
		return ans	
		
a = Solution()
nums1 = [12,24,8,32]; nums2 = [13,25,32,11]		
nums1 = [2,7,11,15]; nums2 = [1,10,4,11]
print(a.advantageCount(nums1, nums2))
			

