from typing import List
class Solution:
	def numRescueBoats(self, people: List[int], limit: int) -> int:
		i, j = 0, len(people) - 1
		boat = 0
		people.sort()
		while i <= j:
			if i < j and people[i] + people[j] <= limit:
				i += 1
			j -= 1	
			boat += 1
			
		return boat

a = Solution()
people = [1,2]; limit = 3			
people = [3,2,2,1]; limit = 3
#people = [3,5,3,4]; limit = 5
#people = [5,1,4,2]; limit = 6
print(a.numRescueBoats(people, limit))
