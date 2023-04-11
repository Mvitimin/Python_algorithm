from typing import List
class Solution:
	def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
		arr.sort()
		ans = []
		n = len(arr)
		for i in range(n - 1):
			diff = ans[-1][1] - ans[-1][0] if ans else float('inf')
			if diff == arr[i + 1] - arr[i]:
				ans.append([arr[i], arr[i + 1]])
			elif arr[i + 1] - arr[i] < diff:
				ans = [[arr[i], arr[i + 1]]]
		return ans

a = Solution()
arr = [4,2,1,3]
arr = [1,3,6,10,15]
arr = [3,8,-10,23,19,-4,-14,27]
print(a.minimumAbsDifference(arr))
				

