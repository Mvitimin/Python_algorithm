from typing import List

class Solution:
	def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
		people.sort(key=lambda x:(-x[0], x[1]))
		ans = []
		for person in people:
			ans.insert(person[1], person)
		return ans

		
a = Solution()
people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
print(a.reconstructQueue(people))		

