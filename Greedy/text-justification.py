from typing import List

class Solution:
	def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
		
		output = []
		line = []
		n = len(words)
		l = 0	
		for i, word in enumerate(words):
			if i == 0 or l + len(word) + len(line) <= maxWidth:
				line.append(word)
				l += len(word)
			else:
				space = len(line) - 1			
				extra = maxWidth - l
				if space == 0:
					txt = line[0] + extra * ' '
				else:
					d, m = divmod(extra, space)
					left, right = d + (1 if m else 0), d
					txt = ''
					for i in range(m):
						txt += (line[i] + ' ' * left)
					txt += (' ' * right).join(line[m:])
				output.append(txt)
				line, l = [word], len(word)
		space = len(line) - 1
		extra = maxWidth - l - space
		txt = ' '.join(line) + ' ' * extra
		output.append(txt)
		return output
			
				
#words = ["This", "is", "an", "example", "of", "text", "justification."]; maxWidth = 16			
#words = ["What","must","be","acknowledgment","shall","be"]; maxWidth = 16	
words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]; maxWidth = 20
a = Solution()
print(a.fullJustify(words, maxWidth))
					
t = 'Science  is  what we'
p = 'Science   is what we'
t = 'This    is    an'
p = 'This    is    an'
