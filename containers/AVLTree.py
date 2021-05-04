'''
This file implements the AVL Tree data structure.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        if not node:
            return True

        left = AVLTree._is_avl_satisfied(node.left)
        right = AVLTree._is_avl_satisfied(node.right)

        if abs(AVLTree._balance_factor(node)) <= 1:
            return right and left
        return False

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.
        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        however, so you will have to adapt their code.
        '''

        r = Node(node.right.value)
        r.right = node.right.right

        nl = Node(node.value)
        nl.left = node.left
        nl.right = node.right.left

        r.left = nl

        return r

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.
        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        however, so you will have to adapt their code.
        '''

        left = Node(node.left.value)
        left.left = node.left.left

        nr = Node(node.value)
        nr.right = node.right
        nr.left = node.left.right

        left.right = nr

        return left

    def insert(self, value):
        '''
        FIXME:
        '''

        if self.root is None:
            self.root = Node(value)
        else:
            self.root = AVLTree._insert(self.root, value)

    @staticmethod
    def _insert(node, value):
        '''
        '''

        if node is None:
            return Node(value)
        elif value < node.value:
            node.left = AVLTree._insert(node.left, value)
        else:
            node.right = AVLTree._insert(node.right, value)

        balance = AVLTree._balance_factor(node)

        if balance > 1 and value < node.left.value:
            return AVLTree._right_rotate(node)
        if balance < -1 and value > node.right.value:
            return AVLTree._left_rotate(node)
        if balance > 1 and value > node.left.value:
            node.left = AVLTree._left_rotate(node.left)
            return AVLTree._right_rotate(node)
        if balance < -1 and value < node.right.value:
            node.right = AVLTree._right_rotate(node.right)
            return AVLTree._left_rotate(node)

        return node
