from typing import List

class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		common = strs[0]
		for i in range(1, len(strs)):
			l = min(len(strs[i]), len(common))
			common = common[:l]
			for j in range(l):
				if strs[i][j] != common[j]:
					common = common[:j]
					break
		return common
		
a = Solution()
strs = ["flower","flow","flight"]
#strs = ["dog","racecar","car"]
#strs = ["", ""]
#strs = ["ab", "a"]
print(a.longestCommonPrefix(strs))

				
				
		
