

class Solution:
	def longestDecomposition(self, text: str) -> int:
		res, l, r = 0, '', ''
		
		for i, j in zip(text, text[::-1]):
			l, r = l + i, j + r
			if l == r:
				res += 1
				l, r = '', ''
		return res

a = Solution()
text = "ghiabcdefhelloadamhelloabcdefghi"
#text = "merchant"
#text = "antaprezatepzapreanta"
print(a.longestDecomposition(text))
