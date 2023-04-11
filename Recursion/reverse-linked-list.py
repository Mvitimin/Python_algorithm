class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def reverseList(self, head: ListNode) -> ListNode:
		if not head:
			return head
		
		def solve(node, prev):
			if not node:
				return prev
			next, node.next = node.next, prev 
			return solve(next, node)
		return solve(head, None)

def makeNodes(nums):
	root = ListNode()
	node = root
	for i in nums:
		node.next = ListNode(i)
		node = node.next
	return root.next 	

def printNode(node):
	while node:
		print('{} - >'.format(node.val), end=' ')
		node = node.next	
							
a = Solution()
head = [1,2,3,4,5]
head = [2, 4]
printNode(a.reverseList(makeNodes(head)))

