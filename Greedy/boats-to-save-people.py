from typing import List
import heapq
class Solution:
	def numRescueBoats(self, people: List[int], limit: int) -> int:
		heap = []
		people.sort(reverse=True)
		boat = 0; 
		for person in people:
			if not heap:
				heapq.heappush(heap, person)
			else:
				if heap[0] + person <= limit:
					heapq.heappop(heap)
					boat += 1
				else:
					heapq.heappush(heap, person)
		return boat + len(heap)

a = Solution()
people = [1,2]; limit = 3			
people = [3,2,2,1]; limit = 3
people = [3,5,3,4]; limit = 5
people = [5,1,4,2]; limit = 6
print(a.numRescueBoats(people, limit))
