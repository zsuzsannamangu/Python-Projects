#This code shows how to store a tree in an array, which is called Sequential Representation of a tree
#Another way to represent trees is Dynamic Node Representation
#Array indexes are values in tree nodes and the value of the root node index would always be -1 as there is no parent for root

#Initialize the tree as a list
tree = []
#Function to insert node in the tree
def insert_node(value):
    #Append the value to the tree list
    tree.append(value)
#Insert nodes into the tree
insert_node(6)
insert_node(3)
insert_node(8)
insert_node(2)
insert_node(4)
insert_node(9)
#Print the tree
print(tree)