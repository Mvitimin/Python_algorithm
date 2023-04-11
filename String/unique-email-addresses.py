from typing import List
import re

class Solution:
	def numUniqueEmails(self, emails: List[str]) -> int:
		for i, email in enumerate(emails):
			s = email.split('@')
			s[0] = re.sub('(\.)|(\+.*)', '', s[0])
			emails[i] = s[0] + '@' + s[1]
		email_set = set(emails)
		return len(email_set)


emails =["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
#emails=["fg.r.u.uzj+o.pw@kziczvh.com","r.cyo.g+d.h+b.ja@tgsg.z.com","fg.r.u.uzj+o.f.d@kziczvh.com","r.cyo.g+ng.r.iq@tgsg.z.com","fg.r.u.uzj+lp.k@kziczvh.com","r.cyo.g+n.h.e+n.g@tgsg.z.com","fg.r.u.uzj+k+p.j@kziczvh.com","fg.r.u.uzj+w.y+b@kziczvh.com","r.cyo.g+x+d.c+f.t@tgsg.z.com","r.cyo.g+x+t.y.l.i@tgsg.z.com","r.cyo.g+brxxi@tgsg.z.com","r.cyo.g+z+dr.k.u@tgsg.z.com","r.cyo.g+d+l.c.n+g@tgsg.z.com","fg.r.u.uzj+vq.o@kziczvh.com","fg.r.u.uzj+uzq@kziczvh.com","fg.r.u.uzj+mvz@kziczvh.com","fg.r.u.uzj+taj@kziczvh.com","fg.r.u.uzj+fek@kziczvh.com"]
a = Solution()
print(a.numUniqueEmails(emails))

'''
text = 'hih.ihi+hihii123_65!#@naver.com'
t = re.compile('[^\@]+').findall(text)
print(t)

res = re.sub('(\.)|(\+[^\@]+)', '', text)
#print(res)
'''
