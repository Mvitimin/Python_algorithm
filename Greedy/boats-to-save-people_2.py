from typing import List

class Solution:
	def numRescueBoats(self, people: List[int], limit: int) -> int:
		
		n = len(people)
		people.sort() 
		i, j = 0, n - 1
		
		ans = 0
		
		while i <= j:
			
			if people[i] + people[j] <= limit:
				i += 1
				j -= 1 
			elif people[i] >= limit:
				ans += n - i
				break
			else:
				j -= 1
			
			ans += 1
		return ans
		

a = Solution()
people = [1,2]; limit = 3
people = [3,2,2,1]; limit = 3
people = [3,5,3,4]; limit = 5
print(a.numRescueBoats(people, limit))
