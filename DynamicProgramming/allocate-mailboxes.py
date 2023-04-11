from typing import List

class Solution:
	def minDistance(self, houses: List[int], k: int) -> int:
		n = len(houses)
		houses.sort()
		sum = [0] * (n + 1)
		for i in range(n):
			sum[i + 1] = sum[i] + houses[i]
		
		def calc(i, j):
			mid1, mid2 = (i + j) // 2, (i + j + 1) // 2 
			return (sum[j + 1] - sum[mid1]) - (sum[mid2] - sum[i])
			
		dp = [float('inf')] * n
		dp = [calc(0, j) for j in range(n)]
				
		for p in range(2, k):
			for j in range(n - 1, p - 2, -1):
				for i in range(p - 2, j):
					dp[j] = dp[i] + calc(i + 1, j)
		
		return dp[-1]
						
			
									
								
											
																	
		return 
a = Solution()
houses = [1,4,8,10,20]; k = 3
#houses = [2,3,5,12,18]; k = 2
#houses = [7,4,6,1]; k = 1
houses = [3, 6, 14, 10]; k = 4
print(a.minDistance(houses, k))
