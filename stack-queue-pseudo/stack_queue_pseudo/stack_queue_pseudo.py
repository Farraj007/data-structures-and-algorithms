# from Stacks_and_Queues.stacks_and_queues import Queue , Stack
class psuedoQueue:
    """
    Implements a Queue using two Stacks.
    """

    def __init__(self):
        self.s1 = []
        self.s2 = []
 
    def enqueue(self, x):
        """
        Inserts value into the PseudoQueue, using a first-in, first-out approach.
        """
    
        while len(self.s1):
            self.s2.append(self.s1[-1])
            self.s1.pop()
             
        self.s1.append(x)
 
        while len(self.s2):
            self.s1.append(self.s2[-1])
            self.s2.pop()
 
    def dequeue(self):
        """
        Extracts a value from the PseudoQueue, using a first-in, first-out approach.
        """
         
        if len(self.s1) == 0:
            print("Q is Empty")
                 
        x = self.s1[-1]
        self.s1.pop()
        return x

 
if __name__ == '__main__':
    q = psuedoQueue()
    print(q.enqueue('hi'))
    q.enqueue('there')
    q.enqueue('!')
 
    # print(q.dequeue())
    # print(q.dequeue())
    # print(q.dequeue())    