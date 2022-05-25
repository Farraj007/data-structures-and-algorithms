def compareTrees(bt1,bt2):
	if getLeafCount(bt1)==getLeafCount(bt2):
			print ('root folders has the same number of files')
	else:
		print ('root folders has a different number of files')

def getLeafCount(node):
	
	if (not node):
		return 0
	q = Queue()
	count = 0 
	q.put(node)
	while (not q.empty()):
		temp = q.queue[0]
		q.get()

		if (temp.left != None):
			q.put(temp.left)
		if (temp.right != None):
			q.put(temp.right)
		if (temp.left == None and
			temp.right == None):
			count += 1
	return count
