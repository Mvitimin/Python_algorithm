from typing import List
import collections

class Solution:
	def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
		map = collections.defaultdict(list)
		for i, c in enumerate(nums2):
			map[c].append(i)
		
		ans = []
		for i, c in enumerate(nums1):
			ans.append(map[c].pop())
		
		return ans

a = Solution()
nums1 = [12,28,46,32,50]; nums2 = [50,12,32,46,28]
nums1 = [84,46]; nums2 = [84,46]
print(a.anagramMappings(nums1, nums2))
