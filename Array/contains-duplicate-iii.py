from typing import List

class Solution:
	def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
		
		buckets = {}
		for i, num in enumerate(nums):
			bucket = num // (t + 1)	
			if bucket in buckets:
				return True
			elif bucket + 1 in buckets and buckets[bucket + 1] - num <= t:
				return True
			elif bucket - 1 in buckets and num - buckets[bucket - 1] <= t:
				return True
			else:
				buckets[bucket] = num
			if i >= k:
				del buckets[nums[i - k] // (t + 1)]			
		return False
		
	
a = Solution()
nums = [1,2,3,1]; k = 3; t = 0
nums = [1,0,1,1]; k = 1; t = 2
nums = [1,5,9,1,5,9]; k = 2; t = 3
print(a.containsNearbyAlmostDuplicate(nums, k, t))			
		
					
			
					
				
			
			
						
					
		

