from typing import List
class Solution:
	def sortArray(self, nums: List[int]) -> List[int]:
		
		def mergeSort(arr):
			if len(arr) <= 1: return arr
			mid = len(arr) // 2
			left = mergeSort(arr[:mid])
			right = mergeSort(arr[mid:])
			
			k = i = j = 0
			m, n = mid, len(arr) - mid 
			while i < m and j < n:
				if left[i] <= right[j]:
					arr[k] = left[i]; i += 1
				else:
					arr[k] = right[j]; j += 1
				k += 1
			
			while i < m:
				arr[k] = left[i]
				i += 1; k += 1
			
			while j < n:
				arr[k] = right[j]
				j += 1; k += 1	
			
			return arr 		
		return mergeSort(nums)
		

a = Solution()
nums = [5, 2, 3, 3, 4, 6, 1]
nums = []
nums = [5,1,1,2,0,0]
nums = [2, 1, 3, 0]
nums = []
print(a.sortArray(nums))
