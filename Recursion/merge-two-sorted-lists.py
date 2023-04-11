from typing import List

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next
class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		if l1 and l2:
			if l1.val < l2.val:
				l1, l2 = l2, l1
			l2.next = self.mergeTwoLists(l1, l2.next)
			return l2
		if l1:
			return l1
		return l2	
		 
def printNode(node):
	while node:
		print('{} ->'.format(node.val), end='')
		node = node.next

def makeListNode(nums: List[int]):
	root = ListNode()
	head = root
	for n in nums:
		head.next = ListNode(n)
		head = head.next			
	return root.next
	
a = Solution()
l1 = [1,2,4]; l2 = [1,3,4]
node1 = makeListNode(l1)
node2 = makeListNode(l2)

#node1 = None
#node2 = ListNode(0)
printNode(a.mergeTwoLists(node1, node2))
