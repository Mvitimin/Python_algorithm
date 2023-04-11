class Solution:
	def wordPattern(self, pattern: str, s: str) -> bool:
		
		splits = s.split()
		if len(pattern) != len(splits):
			return False
		
		alphs = {}	
		words = {}
						
		for i, word in enumerate(splits):
			if pattern[i] in alphs and alphs[pattern[i]] != word:
				return False
			if word in words and words[word] != pattern[i]:
				return False
			
			alphs[pattern[i]] = word
			words[word] = pattern[i]
				
			
		return True
			
a = Solution()
pattern = "abba"; s = "dog cat cat dog"
#pattern = "abba"; s = "dog cat cat fish"
#pattern = "aaaa"; s = "dog cat cat dog"
pattern = "abba"; s = "dog dog dog dog"
print(a.wordPattern(pattern, s))
			
