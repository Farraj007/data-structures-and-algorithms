def find_maximum(self):
        """
        return the maximum value from the binary tree
        input: none
        output: number 
        """
        
        if not self.root:
            raise(Exception("Tree is empty !"))
        
        if not self.root.left and not self.root.right:
            return self.root.value
        
        maximum = self.root.value        
        def _walk(node):
            nonlocal maximum 
            
            if node.value > maximum:
                maximum = node.value
            
            if node.left:
                _walk(node.left)

            if node.right:
                _walk(node.right)
                
        _walk(self.root)
        return maximum
        # if type(maximum) == int:
        #     return int(maximum)
        # else:
        #     raise Exception("Not a number")