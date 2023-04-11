from typing import List

def countingSort(arr: List[int]) -> List[int]:
	n = len(arr)
	m = max(arr)
	counter = [0] * (m + 1)
	output = [0] * n
	for i in range(n):
		counter[arr[i]] += 1
	for i in range(1, m + 1):
		counter[i] += counter[i - 1]	
	for i in range(n):
		j = counter[arr[i]]
		output[j - 1] = arr[i]
		counter[arr[i]] -= 1
	return output
	
arr = [4, 2, 2, 8, 3, 3, 1]
k = countingSort(arr)
print(k)

		
