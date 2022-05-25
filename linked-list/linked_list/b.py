# Python3 program to check if linked
# list is palindrome using stack
class Node:
	def __init__(self,data):
		
		self.value = data
		self.next = None
		
# Function to check if the linked list
# is palindrome or not
def ispalindrome(head):
	
	stack = []
	
	ispalin = True
	while head :
		stack.append(head.value)
		
		head = head.next

	while head:

		i = stack.pop()
		
		if head.data == i:
			ispalin = True
		else:
			ispalin = False
			break
		head = head.ptr
		
	return ispalin

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(3)
six = Node(2)
seven = Node(1)

one.ptr = two
two.ptr = three
three.ptr = four
four.ptr = five
five.ptr = six
six.ptr = seven
seven.ptr = None

result = ispalindrome(one)

print("isPalindrome:", result)

# This code is contributed by Nishtha Goel
