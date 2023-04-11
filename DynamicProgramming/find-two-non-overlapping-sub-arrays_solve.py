#https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/

from typing import List
import sys

class Solution:
	def minSumOfLengths(self, arr: List[int], target: int) -> int:
		
		MAX = sys.maxsize
		minlen = MAX
		ans = MAX
		mins = [MAX] * len(arr)
		left = presum = 0
				
		for right in range(len(arr)):
			
			presum += arr[right]
			while presum > target:
				presum -= arr[left]
				left += 1
			
			if presum == target:
				curlen = right - left + 1
				if left > 0 and mins[left - 1] < MAX:
					ans = min(ans, curlen + mins[left -1])
				minlen = min(curlen, minlen)
			
			mins[right] = minlen	
		
		return -1 if ans == MAX else ans

						
#arr = [3,1,1,1,5,1,2,1]
#target = 3	
arr = [1,2,2,3,2,6,7,2,1,4,8]
target = 5

a = Solution()
print(a.minSumOfLengths(arr, target))
