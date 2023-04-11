from typing import List
import collections
class Solution:
	def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
		txt = ' ' + ' '.join(sentence)
		ans = 0; index = 1; l = len(txt)
		for _ in range(rows):
			index += cols
			if index > l - 1:
				ans += index // l
				index %= l		
			while txt[index] != ' ':
				index -= 1
			index += 1		
		return ans
		
a = Solution()
#sentence = ["a", "bcd", "e"]; rows = 3; cols = 6
sentence = ["hello","world"]; rows = 2; cols = 8
#sentence = ["i","had","apple","pie"]; rows = 4; cols = 5
sentence = ["f","p","a"]; rows = 8; cols = 7
print(a.wordsTyping(sentence, rows, cols))

