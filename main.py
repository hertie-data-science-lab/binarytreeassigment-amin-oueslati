# -*- coding: utf-8 -*-
"""
Submitted on 2nd April 2023

@authors: Oskar Krafft | Paul Sharratt | Fabian Metz | Amin Oueslati
"""

from mlbt import MutableLinkedBinaryTree

lbt = MutableLinkedBinaryTree()

print(len(lbt))
print(lbt.root())

lbt.add_root(1)
lbt.add_left(lbt.root(), 2)
lbt.add_right(lbt.root(), 3)

l = lbt.left(lbt.root())
r = lbt.right(lbt.root())

lbt.add_left(l, 4)
lbt.add_right(l, 5)

lbt.add_left(r, 6)
lbt.add_right(r, 7)

print(len(lbt))
print(lbt.height(lbt.root()))
print()

"""test of traversal methods:
In a Binary Tree, the complexity of the traversal methods is O(n) - whether done recursively or iteratively - since each node is visited exactly once.
We also created an additional breadth-first traversal method, going beyond the assignment's requirements. This included the creation of a linked queue class.
"""
lbt.print_preorder()
lbt.print_postorder()
lbt.print_inorder()
lbt.print_breadthfirst()
