# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:15:46 2023

@author: Hannah
"""

from binarytree import BinaryTree

class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""

    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'
        
        # sets the fundamental parameters of the node
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
    
    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element."""

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')

        if p._container is not self:
            raise ValueError('p does not belong to this container')

        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')
            return p._node
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None


    def __init__(self):
        """Create an intially empty binary tree."""
        self._root = None
        self._size = 0
        self._positions = []
    

    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)

    @property
    def positions(self):
        return self._positions
    
    def parent(self, p):
        """Return the Position of p's parent(or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node._parent)


    def left(self, p):
        """Return the Position of p's left child(or None if no left child)."""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the Position of p's left child(or NOne if no left child)."""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        # it will increase the number if there's elements on right and/or left
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.

        Raise ValueError if tree nonempty.
        """
        # avoid setting root if there's alredy one
        if self._root is not None: raise ValueError('Root already exists. Impossible to add another root.')
        
        # the start size should be 1
        self._size = 1
        
        # seting the givern element e as the root node
        self._root = self._Node(e)
        # giving its position
        pos = self._make_position(self._root)
        self._positions.append(pos)
        
        return pos

    def _add_left(self, p, e):
        """Create a new left child for Position p, storing element e.
        
        Return the Position of new node
        Raise ValueError if Position p is invalidor p already has a left child.
        """

        # calling the validation
        node = self._validate(p)
        
        # checks if the is possible to call this method
        if node._right is not None: raise ValueError('Left child exists')
        
        # increase the original node size
        self._size += 1
        
        # define that the left node will be the element e
        node._left = self._Node(e, node)
        
        # update positions
        pos = self._make_position(node._left)
        self._positions.append(pos)
        
        return pos 

    def _add_right(self, p, e):
        """Create a new right child for Position p, storing element e.
        
        Return the Position of new node
        Raise ValueError if Position p is invalid or p already has a right child.
        """
        # calling the validation
        node = self._validate(p)
        
        # checks if the is possible to call this method
        if node._right is not None: raise ValueError('Right child exists')
        
        # increase the original node size
        self._size += 1
        
        # define that the right node will be the element e
        node._right = self._Node(e, node)
        
        # update position
        pos = self._make_position(node._right)
        self._positions.append(pos)
        return pos


    def _replace(self, p, e):
        """Replace the element at position p with e, and return old element."""
        
        # validate the element
        node = self._validate(p)
        
        # substitue it in the tree
        old = node._element
        node._element = e
        
        return old

    def _delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any.

        Return the element that had been stored at Position p
        Raise ValueError if Position p is invalid or p has two children.
        """

        node = self._validate(p)
        
        # checks if is possible to delete the element
        if self.num_children(p) == 2: raise ValueError('p has two children')
        
        child = node._left if node._left else node._right
        
        # elevate as parent if there's no children
        if child is not None:
            child._parent = node._parent
        
        # turns into root/child
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        
        # update positions
        self._positions.remove(p)
        self._size -= 1
        node._parent = node
        
        return node._element

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p."""
        
        node = self._validate(p)
        
        if not self.is_leaf(p): raise ValueError('position must be leaf')
        
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')
        
        self._size += len(t1) + len(t2)
        
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
            
            
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2.root
            t2._root = None
            t2._size = 0
            

    def preorder(self):
        """Generate a preorder iteration of positions in the tree."""
        
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        """Generate a preorder iteration of positions in subtree rooted at p."""
        
        yield p  # visit p before its subtrees
        for c in self.children(p):
            for other in self._subtree_preorder(c):  # do preorder of c's subtree
                yield other


# Here we introduce the preorder traversal method (root->left->right)

    def preorder_traverse(self, p, depth=0):
        """Perform a recursive pre-order traversal of the tree."""
        
        if p is not None:
            print(" " * depth + "|--", p.element())
            
            if self.left(p) is not None:
                self.preorder_traverse(self.left(p), depth + 1)
                
            if self.right(p) is not None:
                self.preorder_traverse(self.right(p), depth + 1)
  
# Here we introduce the postorder traversal method (left->right->root)

    def postorder_traverse(self, p, depth=0):
        """Perform a recursive post-order traversal of the tree."""
        
        if p is not None:
            
            if self.left(p) is not None:
                self.postorder_traverse(self.left(p), depth + 1)
                
            if self.right(p) is not None:
                self.postorder_traverse(self.right(p), depth + 1)
                
            print(" " * depth + "|--", p.element())

# Here we introduce the inorder traversal method (left->root->right)

    def inorder_traverse(self, p, depth=0):
        """Perform a recursive in-order traversal of the tree."""
        
        if p is not None:
            
            if self.left(p) is not None:
                self.inorder_traverse(self.left(p), depth + 1)

            print(" " * depth + "|--", p.element())
            
            if self.right(p) is not None:
                self.inorder_traverse(self.right(p), depth + 1)

