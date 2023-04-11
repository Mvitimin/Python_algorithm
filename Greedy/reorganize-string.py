import collections

class Solution:
	def reorganizeString(self, S: str) -> str:
		counter = collections.Counter(S)
		common = counter.most_common()
		
		total = sum([common[i][1] for i in range(1, len(common))])
		need = common[0][1] - 1
		
		if common[0][1] > 1 and total < need:
			return ""
		result = []
		for i in range(common[0][1]):
			result.append(common[0][0])
			for j in range(1, len(common)):
				if counter[common[j][0]] > 0 and total >= need:
					result.append(common[j][0])
					counter[common[j][0]] -= 1
					total -= 1
			need -= 1		
		return ''.join(result)

#S = "aaaaacccccbbbbb"
#S = "a"
#S = "vvvlo"
S = "aabbcc"
a = Solution()
print(a.reorganizeString(S))
		
		
