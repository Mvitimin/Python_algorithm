from typing import List

class Solution:
	def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
		
		ans = len(wordsDict)
		idx1 = idx2 = float('-inf')
		
		for i, word in enumerate(wordsDict):
			if word == word1:
				ans = min(ans, i - idx2)
				idx1 = i 
			if word == word2:
				ans = min(ans, i - idx1)
				idx2 = i
		return ans
	
a = Solution()
wordsDict = ["practice", "makes", "perfect", "coding", "makes"]; word1 = "coding"; word2 = "practice"
wordsDict = ["practice" "makes", "perfect", "coding", "makes"]; word1 = "makes"; word2 = "coding"
print(a.shortestDistance(wordsDict, word1, word2))		
				
			
