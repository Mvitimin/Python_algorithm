from typing import List

class Solution:
	def mctFromLeafValues(self, arr: List[int]) -> int:	
		ans = 0
		while len(arr) > 1:
			i = arr.index(min(arr))
			ans += min(arr[i - 1:i] + arr[i + 1:i + 2]) * arr.pop(i)
		return ans
	
a = Solution()
arr = [6,2,4]
arr = [7,12,8,10]
print(a.mctFromLeafValues(arr))
print(arr[-1:0])
