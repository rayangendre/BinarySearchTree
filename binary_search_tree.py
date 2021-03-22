from queue_array import Queue

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self): # Returns empty BST
        self.root = None

    def is_empty(self): # returns True if tree is empty, else False
        if self.root is None:
            return True
        return False

    def search(self, key): # returns True if key is in a node of the tree, else False

        if self.is_empty():
            return False

        if self.search_helper(key, self.root):
            return True


    def search_helper(self, key, root):
        if root is None:
            return False
        if key == root.key:
            return True
        elif key < root.key:
            return self.search_helper(key, root.left)
        
        elif key > root.key:
            return self.search_helper(key, root.right)
        
    



    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        newNode = TreeNode(key, data)

        if (self.is_empty()):
            self.root = newNode
            

        else:
            self.insert_recursion_helper(self.root, newNode)




    def insert_recursion_helper(self, root, newNode):
        if newNode.key == root.key:
            root.data = newNode.data


        elif newNode.key < root.key:
            if root.left is None:
                root.left = newNode
                
            else:
                self.insert_recursion_helper(root.left, newNode)
        
        elif newNode.key > root.key:
            if root.right is None:
                root.right = newNode
                
            else:
                self.insert_recursion_helper(root.right, newNode)
        
        

        



        

    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        currentNode = self.root

        if self.is_empty():
            return None


        while(currentNode.left is not None):
            currentNode = currentNode.left
        
        return (currentNode.key, currentNode.data)

    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        currentNode = self.root

        if self.is_empty():
            return None


        while(currentNode.right is not None):
            currentNode = currentNode.right
        
        return (currentNode.key, currentNode.data)

    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        if self.is_empty():
            return None
        else:
            currentNode = self.root
            return self.tree_height_recursive(currentNode)
        
    def tree_height_recursive(self, currentNode):
        if currentNode is None:
            return -1
        left_height = self.tree_height_recursive(currentNode.left)
        right_height = self.tree_height_recursive(currentNode.right)

        return 1 + max(left_height, right_height)
        


        

    def inorder_list(self): # return Python list of BST keys representing in-order traversal of BST
        if self.is_empty():
            return []
        currentNode = self.root
        return self.inorder_list_recursive(currentNode)

    def inorder_list_recursive(self, currentNode):
        if(currentNode is None):
            return []

        if (currentNode.left is None) and (currentNode.right is None):
            return [currentNode.key]

        leftRoot = self.inorder_list_recursive(currentNode.left)
        rightRoot = self.inorder_list_recursive(currentNode.right)

        keyList = []
        keyList = leftRoot
        keyList.append(currentNode.key)
        keyList = keyList + rightRoot

        return keyList


    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        if self.is_empty():
            return []
        currentNode = self.root
        return self.preorder_list_recursive(currentNode)

    def preorder_list_recursive(self, currentNode):
        if(currentNode is None):
            return []

        if (currentNode.left is None) and (currentNode.right is None):
            return [currentNode.key]

        leftRoot = self.preorder_list_recursive(currentNode.left)
        rightRoot = self.preorder_list_recursive(currentNode.right)

        keyList = []
        keyList = leftRoot
        keyList.insert(0, currentNode.key)
        keyList = keyList + rightRoot

        return keyList

        
    def level_order_list(self):  # return Python list of BST keys representing level-order traversal of BST
        # You MUST use your queue_array data structure from lab 3 to implement this method
        q = Queue(25000) # Don't change this!

        if self.is_empty():
            return []


	
	    # Create an empty queue for level order traversal 
        listOfKeys = []
	

	    # Enqueue Root and initialize height    
        q.enqueue(self.root)
        
        while(not q.is_empty()): 
		    # Print front of queue and remove it from queue 
            node = q.dequeue() 
            listOfKeys.append(node.key)
		    

		    #Enqueue left child 
            if node.left is not None: 
                q.enqueue(node.left) 

		    # Enqueue right child 
            if node.right is not None: 
                q.enqueue(node.right) 
        
        return listOfKeys



