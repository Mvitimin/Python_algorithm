from typing import List

class Solution:
	def maxDistToClosest(self, seats: List[int]) -> int:
		
		people = (i for i, seat in enumerate(seats) if seat)
		prev, future = None, next(people)
		
		
		ans = 0
		for i, seat in enumerate(seats):
			if seat:
				prev = i
			else:
				while future is not None and future < i:
					future = next(people, None)
				
				left = float('inf') if prev is None else i - prev
				right = float('inf') if future is None else future - i
				
				ans = max(ans, min(left, right))
					
				
								
		return ans

a = Solution()
seats = [1,0,0,0,1,0,1]
#seats = [1,0,0,0]
#seats = [0, 1]
print(a.maxDistToClosest(seats))
