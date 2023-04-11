from typing import List
class Solution:
	def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
		arr.sort()
		ans = [[arr[0], arr[1]]]
		diff = arr[1] - arr[0]
		for i in range(1, len(arr) - 1):
			k = arr[i + 1] - arr[i]
			if k < diff:
				ans = [[arr[i], arr[i + 1]]]
				diff = k
			elif k == diff:
				ans.append([arr[i], arr[i + 1]])
				
		return ans

a = Solution()
arr = [4,2,1,3]
#arr = [1,3,6,10,15]
arr = [3,8,-10,23,19,-4,-14,27]
print(a.minimumAbsDifference(arr))
