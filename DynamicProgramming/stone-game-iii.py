from typing import List
class Solution:
	def stoneGameIII(self, stoneValue: List[int]) -> str:
		n = len(stoneValue)
		dp = [[float('-inf')] * 4 for _ in range(n)]
		for i in range(n - 1, -1, -1):
			for j in range(3):
				next = i + j + 1
				dp[i][j] = sum(stoneValue[i:next]) - (dp[next][-1] if next < n else 0)
			dp[i][-1] = max(dp[i][:])
			
		print(dp)	
		if dp[0][-1] > 0:
			return 'Alice'
		elif dp[0][-1] < 0:
			return 'Bob'
		return 'Tie'
		
	
a = Solution()
stoneValue = [0, 1, 2, -3, -4, 5, -6]
values = [1, 2, 3, 7]
#values = [1, 2, 3, -9]
#values = [1,2,3,6]
#values = [1,2,3,-1,-2,-3,7]
#values = [-1,-2,-3]
print(a.stoneGameIII(values))
				
				
