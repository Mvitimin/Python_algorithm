import re


class Solution:
	chunk_ip4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
	pattern_ip4 = re.compile(r'^(' + chunk_ip4 + r'\.){3}' + chunk_ip4 + r'$')
	chunk_ip6 = r'([0-9a-fA-F]{1,4})'
	pattern_ip6 = re.compile(r'^(' + chunk_ip6 + r'\:){7}' + chunk_ip6 + r'$')
		
	def validIPAddress(self, queryIP: str) -> str:
		
		if self.pattern_ip4.match(queryIP):
			return "IPv4"
		return "IPv6" if self.pattern_ip6.match(queryIP) else "Neither"

a = Solution()
queryIP = "172.16.254.1"
queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
#queryIP = "01.01.01.01"
#queryIP = "256.256.256.256"

print(a.validIPAddress(queryIP))				



