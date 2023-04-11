from typing import List

class Solution:
	def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
		tokens.sort()
		n = len(tokens)
		if power >= sum(tokens): return n
		i, j = 0, len(tokens) - 1
		score = ans = 0
		while i <= j:
			if score == 0 and tokens[i] > power:
				break
			
			while tokens[i] <= power and i <= j:
				power -= tokens[i]
				i += 1
				score += 1
			
			ans = max(score, ans)
			
			while score > 0 and tokens[i] > power and i <= j:
				power += tokens[j]
				j -= 1
				score -= 1
				
		return ans		
				
				
a = Solution()
tokens = [100,200,300,400]; power = 200
tokens = [100,200]; power = 150
tokens = [100]; power = 50
print(a.bagOfTokensScore(tokens, power))		
						
				
