from typing import List

class Solution:
	
	def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
		n = len(books)
		dp = [float('inf')] * (n + 1)
		dp[0] = books[0][1]
		dp[-1] = 0
		for i in range(1, n):
			dp[i] = dp[i - 1] + books[i][1]
			cur_width, cur_height = books[i]
			for j in range(i - 1, -1, -1):
				cur_width += books[j][0]
				if cur_width > shelf_width:
					break
				cur_height = max(cur_height, books[j][1])
				dp[i] = min(dp[i], dp[j - 1] + cur_height)
		return dp[n - 1]		
			
			
							
a = Solution()
books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelf_width = 4
print(a.minHeightShelves(books, shelf_width))
