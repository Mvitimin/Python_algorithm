from typing import List

class Solution:
	def sumOddLengthSubarrays(self, arr: List[int]) -> int:
		n = len(arr)
		ans = 0
		for i in range(n):
			odd = ((i + 1) * (n - i) + 1) // 2
			ans += odd * arr[i]
		return ans

a = Solution()
arr = [1,4,2,5,3]
arr = [1,2]
arr = [10,11,12]
print(a.sumOddLengthSubarrays(arr))
			
		
