from typing import List
from functools import lru_cache

class Solution:
	
	def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
		n = len(books)
		prev_max_height, max_height = 0, books[0][0]
		
		@lru_cache(None)
		def helper(index, width, max_height):
			if index >= n:
				return max_height
			if width + books[index][0] > shelf_width:
				return float('inf')
			max_height = max(max_height, books[index][1])
			ans = min(helper(index + 1, width + books[index][0], max_height), max_height + helper(index + 1, 0, 0))
			return ans
		return helper(0, 0, 0)	
		
			
				
				
						
a = Solution()
books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]
shelf_width = 4
print(a.minHeightShelves(books, shelf_width))
