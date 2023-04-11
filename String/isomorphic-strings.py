class Solution:
	def isIsomorphic(self, s: str, t: str) -> bool:
		m, n = len(s), len(t)
		if m != n:
			return False
		
		maps1 = {}
		maps2 = {}
		
		
		for i in range(n):
			if s[i] in maps1 and maps1[s[i]] != t[i]:
				return False		
			if t[i] in maps2 and maps2[t[i]] != s[i]:
				return False
			maps1[s[i]] = t[i]
			maps2[t[i]] = s[i]				
		return True

a = Solution()
s = "egg"; t = "add"
#s = "foo"; t = "bar"
#s = "paper"; t = "title"
s = "badc"; t = "baba"
print(a.isIsomorphic(s, t))
						


