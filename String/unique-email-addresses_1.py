import re
from typing import List

class Solution:
	def numUniqueEmails(self, emails: List[str]) -> int:
		
		seen = set()
		for email in emails:
			idx = email.index('@')
			local, domain = email[:idx], email[idx:]
			local = re.sub('\.|(\+.+)', '', local)
			seen.add('{}{}'.format(local, domain))
		return len(seen)
		
a = Solution()
emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]



print(a.numUniqueEmails(emails))

p = "test.email+alex"
print(re.sub('\.|(\+.+)', '', p))



