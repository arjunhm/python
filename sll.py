"""
Program to demonstrate Single Linked List
"""

import sys

class Node():

	def __init__(self, data):
		self.data = data
		self.next = None

	def get_data(self):
		return self.data



class LinkedList():

	def __init__(self):
		self.head = None

	def ins_end(self, data):
		new_node = Node(data)

		if not self.head:			#if LL has no node
			self.head = new_node

		else:

			if not self.head.next:	#if LL has only one node 
				self.head.next = new_node

			else:
				curptr = self.head

				while curptr.next:
					curptr = curptr.next

				curptr.next = new_node


	def ins_front(self, data):
		new_node = Node(data)

		if not self.head:
			self.head = new_node

		else:
			new_node.next = self.head
			self.head = new_node


	def del_end(self):

		if not self.head:
			print("List is empty")

		elif not self.head.next:
			self.head = None

		else:
			curptr = self.head
			while curptr.next:
				prev_ptr = curptr
				curptr = curptr.next

			curptr = None
			prev_ptr.next = None


	def del_front(self):
		if not self.head:
			print("List is empty")

		else:
			self.head = self.head.next

	def display(self):

		if not self.head:
			print("List is empty")

		else:
			curptr = self.head

			while curptr:
				print(curptr.get_data())
				curptr = curptr.next


sll = LinkedList()

while 1:

	print("STACK MENU")
	print("1. Insert at front\n2. Insert at end\n3. Delete from front")
	print("4. Delete from end\n5. Display\n6. Exit")

	choice = int(input('Enter your choice:'))

	if choice == 1:
		value = int(input('Enter a value:'))
		sll.ins_front()

	elif choice == 2:
		value = int(input('Enter a value:'))
		sll.ins_end()

	elif choice == 3:
		sll.del_front()

	elif choice == 4:
		sll.del_end()

	elif choice == 5:
		sll.display()

	elif choice == 6:
		sys.exit()
	else:
		print("Invalid choice")
