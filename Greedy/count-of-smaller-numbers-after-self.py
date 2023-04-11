from typing import List

class Solution:
	def countSmaller(self, nums: List[int]) -> List[int]:
		if not nums:
			return []
		n = len(nums)
		nums = [(nums[i], i) for i in range(n)]
		res = [0] * n 
		
		def merge(arr):
			
			if len(arr) == 1:
				return arr 
			
			mid = (len(arr) - 1) // 2
			left = merge(arr[:mid + 1])
			right = merge(arr[mid + 1:])
			merged, i, j = [], 0, 0
			inversions = 0
			
			while i < len(left) or j < len(right):
				if i == len(left):
					merged.append(right[j])
					j += 1
				elif j == len(right):
					index = left[i][1]
					res[index] += inversions
					merged.append(left[i])
					i += 1
					print(left, right, inversions, merged)			
				elif right[j][0] < left[i][0]:
					merged.append(right[j])
					inversions += 1
					j += 1
				else:
					index = left[i][1]
					res[index] += inversions
					merged.append(left[i])
					i += 1
			return merged
			
		merge(nums)
		return res

''''
class Solution:
	def countSmaller(self, nums: List[int]) -> List[int]:
		n = len(nums)
		arr = [[v, i] for i, v in enumerate(nums)]	
		result = [0] * n 
		def merge_sort(arr, left, right):
			if right - left <= 1:
				return 
			mid = (left + right) // 2
			merge_sort(arr, left, mid)
			merge_sort(arr, mid, right)
			merge(arr, left, right, mid)
			
		def merge(arr, left, right, mid):
			i, j = left, mid
			temp = []
			print(arr, left, right, mid)
			while i < mid and j < right:
				if arr[i][0] <= arr[j][0]:
					result[arr[i][1]] += j - mid 
					temp.append(arr[i])
					i += 1
				else:
					temp.append(arr[j])
					j += 1
			
			while i < mid:
				result[arr[i][1]] += j - mid
				temp.append(arr[i])
				i += 1
			while j < right:
				temp.append(arr[j])
				j += 1
			
			for i in range(left, right):
				arr[i] = temp[i - left]	
						
		merge_sort(arr, 0, n)		
		return result 
'''		
		
a = Solution()
nums = [5,2,6,1]
print(a.countSmaller(nums))
#print(bisect.bisect_left([1, 2, 3, 4], 0))
