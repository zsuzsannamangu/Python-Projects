#Binary tree is a tree with two nodes
#Binary Search Tree (BST) is where the nodes with lesser values are placed to the left 
#of the root, and nodes with greater or equal values are placed to the right. So you can easily find elements according to this rule.
#When you are searching for an element, you first look at the root, and you determine whether the searched value will be on its left or right,
#When you know that, you go to that element and again determine whether the searched value will be on its left or right (lesser, equal or greater), etc.

#function to search a given key in a given BST
class Node:
    #The __init__ method is used as a constructor, to initalize objects of a class
    #The keyword "self" represents the instance of a class
    def __init__(self, key):
        self.key = key #Value of the node
        self.left = None #Reference to the left child node
        self.right = None #Reference to the right child node

class BinarySearchTree:
    def __init__(self):
        self.root = None #Reference to the root node of the binary search tree
    
    #A function to insert a new node with the given key in BST
    def insert(self, key):
        if self.root is None: #If the tree is empty
            self.root = Node(key) #Create a new node and set it as the root
        else: #Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands
            #Imagine you have a deck of cards that needs to be sorted. In recursive insertion sort, you start with an empty hand (sorted portion) and 
            #pick one card at a time from the pile (unsorted portion). You insert each card in its correct position in your hand until all cards are in order.
            self._insert_recursive(self.root, key) #Call the recursive index function with the root

    def _insert_recursive(self, node, key):
        if key < node.key: #If the key is less than the current node's key
            if node.left is None: #if the left child is empty
                node.left = Node(key) #Create a new node and set it as the left child
            else:
                self._insert_recursive(node.left, key) #Recursively insert in the left subtree:
                #so look at what is already there and insert it into the correct position in relation to the other values
        else: #if the key is greater or equal to the current node's key
            if node.right is None: #if the right child is empty
                node.right = Node(key) #Create a new node and set it as the right child
            else:
                self._insert_recursive(node.right, key) #Recursively insert the right subtree

    def search(self, key):
        return self._search_recursive(self.root, key) #Call the recursive search function with the root
    
    def _search_recursive(self, node, key):
        if node is None or node.key == key: #If the node is None or the key is found
            return node #Return the node(found) or None(not found)
        if key < node.key: #If the key is less than the current node's key
            return self._search_recursive(node.left, key) #Recursively search in the left subtree:
        #so look at what is there and search in order according to BST rules: lesser values are on the left, greater or equal values are on the right
        else:
            return self._search_recursive(node.right, key) #Recursively search in the right subtree
        
#Test the Binary Search Tree
bst = BinarySearchTree() #Create a new BST object

#Insert nodes into the newly created BST object
bst.insert(5)
bst.insert(3)
bst.insert(8)
bst.insert(2)
bst.insert(4)
bst.insert(7)

#Search for a given key
print(bst.search(4).key) #Print the key of the node(there is 4, so it will be 4)
print(bst.search(10)) #Print the key of the node(there is no 10, so it won't find it, it will be: None)
