# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:31:59 2023

@author: Hannah
"""

from linkedbinarytree import LinkedBinaryTree

class MutableLinkedBinaryTree(LinkedBinaryTree):
    
    # The hidden implementation is around the class LinkedBinaryTree
    """
    Provides public wrapper functions for each of the inherited nonpublic update methods.
    """
    # method to add an element to the root
    def add_root(self, e):
        return self._add_root(e)
    
    # add to the left side
    def add_left(self, p, e):
        return self._add_left(p, e)
    
    # add to the right side
    def add_right(self, p, e):
        return self._add_right(p, e)

    # calls the replacement method
    def replace(self, p, e):
        return self._replace(p, e)
    
    # exclude an element
    def delete(self, p):
        return self._delete(p)
    
    # attachs an element
    def attach(self, p, T1, T2):
        return self.attach(p, T1, T2)
    