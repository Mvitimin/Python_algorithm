
class Solution:
	def checkValidString(self, s: str) -> bool:
		minL = maxL = 0 
		for i, c in enumerate(s):
			minL += 1 if c == '(' else -1
			maxL += 1 if c != ')' else -1
			if maxL < 0: return False
			minL = max(minL, 0)		
		return minL == 0

a = Solution()
s = "(*)()((***))"
s = "**"
print(a.checkValidString(s))
