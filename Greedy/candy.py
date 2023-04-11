from typing import List

class Solution:
	def candy(self, ratings: List[int]) -> int:
		n = len(ratings)
		dp = [1] * n 
		turns = []
		for i in range(n):
			turns.append((ratings[i], i))
		turns.sort(key=lambda x:x[0])
		
		for r, i in turns:
			for j in [i + 1, i - 1]:
				if 0 <= j < n and ratings[j] > r:
					dp[j] = max(dp[j], dp[i] + 1)
										
		return sum(dp)	
		
a = Solution()
ratings = [1, 0, 2]
ratings = [1,2,2]
ratings = [1, 4, 5, 3, 2, 1]
ratings = [2, 1, 5, 1, 3, 3, 5, 7, 4]
print(a.candy(ratings))
