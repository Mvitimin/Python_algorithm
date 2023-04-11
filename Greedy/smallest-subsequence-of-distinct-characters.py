import collections

class Solution:
	def smallestSubsequence(self, s: str) -> str:
		
		counter = collections.Counter(s)
		unique = len(counter)
		stack = []
		seen = set()
		
		for i, c in enumerate(s):
			while stack and c not in seen and stack[-1] > c and counter[stack[-1]] > 0:
				seen.remove(stack.pop())
			counter[c] -= 1
			if c not in seen:
				stack.append(c)
				seen.add(c)
		return ''.join(stack)
a = Solution()
s = "cbacdcbc"
#s = "bcabc"
#s = "cbaacabcaaccaacababa"
#s = "leetcode"
#s = "dbbbabadcdcbdaddddbbcbdaaadbdaadcaaabbab"
#s = "adaabbcacdbabaeabebc"
print(a.smallestSubsequence(s))		
				
		
