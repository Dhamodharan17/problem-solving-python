class Solution:
    #Function to insert a node in a BST. 
    def insert(self,root, Key):
        
        if root == None:
            return Node(Key)
        
        #When already present
        if root.data == Key:
            return root
            
        #when key is less -> it should left
        if root.data > Key:
            root.left = self.insert(root.left, Key)
        
        else:
            root.right = self.insert(root.right, Key)
         
        return root 

