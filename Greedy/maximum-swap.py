class Solution:
	def maximumSwap(self, num: int) -> int:
		arr = list(str(num))
		n = len(arr)
		i, j = 0, 0
		max_idx, max_val = -1, arr[-1]  
		for k in range(n - 2, -1, -1):
			if arr[k] > max_val:
				max_idx, max_val = k, arr[k] 
			elif arr[k] < max_val:
				i, j = k, max_idx
		
		arr[i], arr[j] = arr[j], arr[i]				
		return int(''.join(arr))
		
a = Solution()
nums = 2736
nums = 98368
#nums = 1993
#nums = 9973
print(a.maximumSwap(nums))
				
		

