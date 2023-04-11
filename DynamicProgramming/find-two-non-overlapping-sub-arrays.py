#https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/

from typing import List

class Solution:
	def minSumOfLengths(self, arr: List[int], target: int) -> int:
		list_t = []
		dp = [arr[0]]
		if dp[0] == target:
			list_t.append(0)
		
		for i in range(1, len(arr)):
			sum_v = dp[i - 1] + arr[i]
			if arr[i - 1] + arr[i] == target:
				sum_v = arr[i - 1] + arr[i]
		
			if sum_v == target or arr[i] == target:
				list_t.append(i)
			
			if sum_v >= target:
				dp.append(arr[i])
			else:
				dp.append(sum_v)
		
		if len(list_t) < 2:
			return -1
		
		list_t.sort(reverse=True)
		start = len(arr)
		comp = len(arr)
		lenghts = []
		for idx in list_t:
			if idx >= start:
				comp = lenghts.pop()				
			sum_v = arr[idx]
			start = idx
			while sum_v < target:
				start -= 1
				sum_v += arr[start]
			
			lenght = min(comp, idx - start + 1)	
			lenghts.append(lenght)
			comp = len(arr)				
		
		if len(lenghts) < 2:
			return - 1
		lenghts.sort()
		return lenghts[0] + lenghts[1]	
		

						
#arr = [3,1,1,1,5,1,2,1]
#target = 3	
arr = [1,2,2,3,2,6,7,2,1,4,8]
target = 5

a = Solution()
print(a.minSumOfLengths(arr, target))
