from typing import List

class Solution:
	def pancakeSort(self, arr: List[int]) -> List[int]:
		n = len(arr)
		for i in range(n):
			if arr[i] != i + 1:
				break
		else: return []
					
		ans = []
		for i in range(n, 1, -1):
			if arr[0] != i:
				j = arr.index(i)
				arr = arr[j::-1] + arr[j + 1:]
				ans.append(j + 1)	
			ans.append(i)		
			arr[:i] = arr[i - 1::-1]
		return ans	
		
a = Solution()

arr = [3, 5, 4, 1, 2]
arr = [3, 2, 4, 1]
print(a.pancakeSort(arr))
#print(arr[3:0:-1])					

def bubbleSort(arr):
	n = len(arr)
	for _ in range(n):
		for i in range(n - 1):
			if arr[i] > arr[i + 1]:
				arr[i], arr[i + 1] = arr[i + 1], arr[i]

def pancakeSort(A):
	res = []
	for x in range(len(A), 1, -1):
		i = A.index(x)
		res.extend([i + 1, x])
		A = A[:i:-1] + A[:i]
	return res
#print(pancakeSort([1, 2, 3, 4]))""
