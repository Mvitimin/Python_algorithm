from typing import List

class Solution:
	def validMountainArray(self, arr: List[int]) -> bool:
		
		n = len(arr)
		
		if len(arr) < 3 or arr[0] >= arr[1]:
			return False 

		flag = False
		
		for i in range(1, n - 1):
			if arr[i] == arr[i + 1]:
				return False
			if not flag and arr[i] > arr[i + 1]:
				flag = True
			elif flag and arr[i - 1] < arr[i]:
				return False	
				
		return arr[n - 2] > arr[n - 1]									

a = Solution()
arr = [2, 1]
arr = [3, 5, 5]
arr = [0, 3, 2, 1]
print(a.validMountainArray(arr))
