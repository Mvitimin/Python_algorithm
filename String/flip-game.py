from typing import List

class Solution:
	def generatePossibleNextMoves(self, currentState: str) -> List[str]:
		ans = []
		for i in range(len(currentState) - 1):
			if currentState[i] == currentState[i + 1] and currentState[i] == '+':
				ans.append(currentState[:i] + '--' + currentState[i + 2:])
		return ans

a = Solution()
currentState = "++++"
print(a.generatePossibleNextMoves(currentState))

