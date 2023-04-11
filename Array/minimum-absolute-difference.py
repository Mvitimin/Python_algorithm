from typing import List

class Solution:
	def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
		arr.sort()
		n = len(arr)
		stack = [[arr[0], arr[1]]]
		for i in range(1, n - 1):
			diff = arr[i + 1] - arr[i]
			if (stack[-1][1] - stack[-1][0]) < diff: continue		
			while stack and (stack[-1][1] - stack[-1][0]) > diff:
				stack.pop()
			stack.append([arr[i], arr[i + 1]])	
		return stack		

a = Solution()
arr = [4, 2, 1, 3]
arr = [1,3,6,10,15]
arr = [3,8,-10,23,19,-4,-14,27]
print(a.minimumAbsDifference(arr))
				
		

