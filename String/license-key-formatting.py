class Solution:
	def licenseKeyFormatting(self, s: str, k: int) -> str:
		characters = ''.join(s.split('-')).upper()
		ans = []
		j = 0
		for i in range(len(characters) - 1, -1, -1):
			if j == k:
				ans.append('-')
				j = 0
			j += 1
			ans.append(characters[i])
		return ''.join(reversed(ans))
		
		
a = Solution()
s = "5F3Z-2e-9-w"; k = 4
s = "2-5g-3-J"; k = 2
print(a.licenseKeyFormatting(s, k))
