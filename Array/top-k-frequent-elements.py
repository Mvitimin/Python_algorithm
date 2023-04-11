from typing import List
import collections
import random
class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		counter = collections.Counter(nums)
		keys = list(counter.keys())
		n = len(keys)
		def findKthLargest(arr, idx):
			l, r = 0, n - 1
			while l <= r:
				i, pivot = l, random.randint(l, r)
				arr[pivot], arr[r] = arr[r], arr[pivot]
					
				for j in range(l, r):
					if counter[arr[j]] <= counter[arr[r]]:
						arr[j], arr[i] = arr[i], arr[j]
						i += 1
				
				arr[i], arr[r] = arr[r], arr[i]
				
				if i > idx:
					r = i - 1
				elif i < idx:
					l = i + 1
				else:
					return arr[i:]			
				
		return findKthLargest(keys, n - k)		
							
a = Solution()
nums = [1,1,1,2,2,3]; k = 2			
#nums = [1]; k = 1
nums = [5,-3,9,1,7,7,9,10,2,2,10,10,3,-1,3,7,-9,-1,3,3]; k = 3
nums = [-1,1,4,-4,3,5,4,-2,3,-1]; k = 3
print(a.topKFrequent(nums, k))						
					
			
			
		
		

