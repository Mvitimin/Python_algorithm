from typing import List

class Solution:
	def maxJumps(self, arr: List[int], d: int) -> int:
		n = len(arr)
		dp = [1] * n 
		events = [[arr[i], i] for i in range(n)]
		events.sort(reverse=True)
		
		for height, index in events:
			for i in range(1, d + 1):
				if index + i < n and arr[index + i] < height:
					dp[index + i] = max(dp[index] + 1, dp[index + i]) 
				else:
					break
			for i in range(1, d + 1):	
				if index - i >= 0 and arr[index - i] < height:
					dp[index - i] = max(dp[index] + 1, dp[index - i])
				else:
					break
		
		return max(dp)
	
a = Solution()					
arr = [6,4,14,6,8,13,9,7,10,6,12]
d = 2
arr = [3,3,3,3,3]
d = 3
arr = [7,6,5,4,3,2,1]
d = 1
arr = [7,6,5,4,3,2,1]
d = 1
arr = [7,1,7,1,7,1]
d = 2
arr = [66]
d = 1
print(a.maxJumps(arr, d))
