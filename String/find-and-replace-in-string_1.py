from typing import List
class Solution:
	def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
		ans = []
		arr = list(S)
		for i, s, t in sorted(zip(indexes, sources, targets), reverse=True):
			if all([arr[item] == s[item - i] for item in range(i, i + len(s))]):
				arr[i:i + len(s)] = list(t)
		return ''.join(arr) 

a = Solution()
S = "abcd"
indexes = [0, 2]
sources = ["ab","ec"]
targets = ["eee","ffff"]
print(a.findReplaceString(S, indexes, sources, targets))
			
