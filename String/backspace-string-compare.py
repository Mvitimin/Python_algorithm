class Solution:
	def backspaceCompare(self, s: str, t: str) -> bool:
		m, n = len(s), len(t)
		
		i, j = m - 1, n - 1
		
		def back(i, string):
			if i < 0 or string[i] != '#':
				return i
			backspace, i = 1, i - 1
			while i >= 0 and backspace:
				backspace += (1 if string[i] == '#' else -1)
				i -= 1
			return back(i, string)
			
		
		while i >= 0 or j >= 0:
			
			i, j = back(i, s), back(j, t)
			
			if (i < 0 and j < 0) or (i >= 0 and j >= 0 and s[i] == t[j]):
				i -= 1
				j -= 1
			else:
				return False
				
		return True

a = Solution()
s = "ab#c"; t = "ad#c"
#s = "ab##"; t = "c#d#"
#s = "a#c"; t = "b"
#s = "ab##"; t = "a#b#"
s = "bxj##tw"; t = "bxo#j##tw"
#s = "a##c"; t = "#a#c"
#s = "bxj##tw"; t = "bxj###tw"
print(a.backspaceCompare(s, t))		

