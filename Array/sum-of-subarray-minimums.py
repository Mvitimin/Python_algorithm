from typing import List
class Solution:
	def sumSubarrayMins(self, arr: List[int]) -> int:
		stack = [-1]
		arr.append(-1)
		ans = 0
		for i in range(len(arr)):
			while arr[stack[-1]] > arr[i]:
				index = stack.pop()
				ans += arr[index] * (i - index) * (index - stack[-1])
			stack.append(i)	
		return ans % (10 ** 9 + 7)
	
a = Solution()
arr = [3,1,2,4]
print(a.sumSubarrayMins(arr))
