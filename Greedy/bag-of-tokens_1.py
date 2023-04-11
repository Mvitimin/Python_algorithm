from typing import List
class Solution:
	def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
		n = len(tokens)
		tokens.sort()
		i, j = 0, n - 1
		score = 0
		
		while i <= j:
			if tokens[i] <= power:
				power -= tokens[i]
				score += 1
				i += 1
			else:
				if score and i < j:
					power += tokens[j]
					score -= 1
					j -= 1
				else: 
					break
		return score
				
				
a = Solution()
tokens = [100]; power = 50
tokens = [100,200]; power = 150
#tokens = [100,200,300,400]; power = 200
print(a.bagOfTokensScore(tokens, power))				
