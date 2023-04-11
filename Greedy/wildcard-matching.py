class Solution:
	def isMatch(self, s: str, p: str) -> bool:
		dp = {}
		def removeDuplicated(p):
			if p == '':
				return p
			tmp = [p[0]]
			for x in p[1:]:
				if tmp[-1] != '*' or tmp[-1] == '*' and x != '*':
					tmp.append(x)
			return ''.join(tmp)
			
		def helper(s, p):
			if (s, p) in dp:
				return dp[(s, p)]
			if p == s: dp[(s, p)] = True
			elif p == '*': dp[(s, p)] = True
			elif s == '' or p == '': dp[(s, p)] = False
			elif s[0] == p[0] or p[0] == '?': dp[(s, p)] = helper(s[1:], p[1:])
			elif p[0] == '*': dp[(s, p)] = helper(s[1:], p) or helper(s, p[1:])
			else:	dp[(s, p)] = False
			return dp[(s, p)]
		
		return helper(s, removeDuplicated(p))

a = Solution()
s = "adceb"; p = "*a*b"
s = "acdcb"; p = "a*c?b"
print(a.isMatch(s, p))
	
