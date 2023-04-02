# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:18:23 2023

@author: Hannah
"""
# Import the class
from mlbt import MutableLinkedBinaryTree

# initiate the class MutableLinkedBinaryTree
lbt = MutableLinkedBinaryTree()


# Now, the tests and friendly outputs to show our classes

print("Welcome to our abstract binary tree class! 🌳🌴🎄")
print("Altough abstract, this tree represents data in a very useful way for many apllications.")
print("It's very versitle and mutable: it can store HTML tags, XML files or even file structures.")
print("Veery powerful, right? 🤩 (and, well, probably very ecological too 🌳🌳🌳)")

print("\n")
print("--- Let's start for the root of the tree ---")
print("So far, the lenght of our tree is:", len(lbt))
print("And our root is empty:", lbt.root())
print("\n")

# Adding element 1 to the root
lbt.add_root(1)
print("Now our root has an element:", lbt.root())

# After presentin the class, we'll add several elements
# to show how this works

# Add the element 2 to the root
lbt.add_left(lbt.root(), 2)

# and add the element 3
lbt.add_right(lbt.root(), 3)
print("\n")

# Creat the left child
l = lbt.left(lbt.root())
print("The left child:", l)

# And the right one
r = lbt.right(lbt.root())
print("The right child:", r)

# Adding the element 4 in the left of branch l
lbt.add_left(l, 4)

# Adding the element 5 in the right of branch l
lbt.add_right(l, 5)

# Adding the element 6 in the left of branch r
lbt.add_left(r, 6)

# Adding the element 7 in the right of branch r
lbt.add_right(r, 7)

# Show the user the results of the operations above
print("\n")
print("Now our tree has grown!")
print("The size of the tree:", len(lbt))
print("Let's check how tall is our tree!")
print("The heigh from the root is", lbt.height(lbt.root()))
print("\n")

# Performing a preorder traverse on our binary tree
print("Here is the preorder traverse")
print("\n")
lbt.preorder_traverse(lbt.root())
print("\n")

# Performing a postorder traverse on our binary tree
print("Here is the postorder traverse")
print("\n")
lbt.postorder_traverse(lbt.root())
print("\n")

# Performing an inorder traverse on our binary tree
print("Here is the inorder traverse")
print("\n")
lbt.inorder_traverse(lbt.root())
