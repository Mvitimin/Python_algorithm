class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


def printNode(root):
	while root:
		print(root.val, end='->')
		root = root.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

root = ListNode(5)
root.next = head
head = head.next
printNode(root)

