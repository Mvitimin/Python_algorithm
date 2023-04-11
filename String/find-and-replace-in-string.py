from typing import List

class Solution:
	def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
		ans, i = [], 0
		while i < len(S):
			if i in indexes:
				j = indexes.index(i)
				r = S[i: len(sources[j]) + i]
				if r == sources[j]:
					ans.append(targets[j])
				else:
					ans.append(r)
				i += len(r)
			else:
				ans.append(S[i])
				i += 1				
		return ''.join(ans)

a = Solution()
'''
S = "abcd"
indexes = [0, 2]
sources = ["a", "cd"]
targets = ["eee", "ffff"]
'''
S = "abcd"
indexes = [0, 2]
sources = ["ab","ec"]
targets = ["eee","ffff"]
print(a.findReplaceString(S, indexes, sources, targets))
			
