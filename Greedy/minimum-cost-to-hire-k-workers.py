from typing import List
from fractions import Fraction
import heapq
class Solution:
	def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
		workers = sorted((Fraction(w, q), q, w) for q, w in zip(quality, wage))
		ans = float('inf')
		heap = []
		sumq = 0 
		
		print(workers)
		for ratio, q, w in workers:
			heapq.heappush(heap, -q)
			sumq += q
		
			if len(heap) > k:
				sumq += heapq.heappop(heap)
			if len(heap) == k:
				print(heap, ratio, sumq)
				ans = min(ans, ratio * sumq)
				
		return float(ans)
		
	
a = Solution()
quality = [10,20,5]; wage = [70,50,30]; k = 2	
quality = [3,1,10,10,1]; wage = [4,8,2,2,7]; k = 3
print(a.mincostToHireWorkers(quality, wage, k))		
		
		
