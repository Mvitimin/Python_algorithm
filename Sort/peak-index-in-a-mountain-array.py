from typing import List

class Solution:
	def peakIndexInMountainArray(self, arr: List[int]) -> int:
		lo, hi = 0, len(arr) - 1
		while lo < hi:
			mid = lo + (hi - lo) // 2
			if arr[mid] < arr[mid + 1]:
				lo = mid + 1
			else: hi = mid
		return lo
												
a = Solution()
arr = [0,1,0]
arr = [0,2,1,0]
arr = [0,10,5,2]
#arr = [3,4,5,1]
#arr = [24,69,100,99,79,78,67,36,26,19]
print(a.peakIndexInMountainArray(arr))

