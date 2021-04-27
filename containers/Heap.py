'''
'''
from containers.BinaryTree import BinaryTree, Node


class Heap(BinaryTree):
    '''
    FIXME:
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the Heap.
        '''
        super().__init__()
        if xs:
            self.insert_list(xs)

    def __repr__(self):
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        '''
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        '''
        FIXME:
        Implement this method.
        The lecture videos have the exact code you need,
        '''
        left = True
        right = True

        if node.left:
            if node.value > node.left.value:
                return False
            else:
                left = Heap._is_heap_satisfied(node.left)
        if node.right:
            if node.value > node.right.value:
                return False
            else:
                right = Heap._is_heap_satisfied(node.right)

        return right and left

    def insert(self, value):
        '''
        Inserts value into the heap.
        '''
        if self.root is None:
            self.root = Node(value)
            self.root.descendents = 1
        else:
            self.root = Heap._insert(self.root, value)

    @staticmethod
    def _insert(node, value):
        '''
        FIXME:
        Implement this function.
        '''
        if node is None:
            return

        if node.left and node.right:
            node.left = Heap._insert(node.left, value)
            if node.value > node.left.value:
                return Heap._move_up(node, value)

        if node.left is None:
            node.left = Node(value)
            if node.value > node.left.value:
                return Heap._move_up(node, value)

        elif node.right is None:
            node.right = Node(value)
            if node.value > node.right.value:
                return Heap._move_up(node, value)

        return node

    @staticmethod
    def _move_up(node, value):
        '''
        '''

        if Heap._is_heap_satisfied(node):
            return node
        if node.left and node.left.value > node.value:
            node.left = Heap._move_up(node.left, value)
        if node.right and node.right.value > node.value:
            node.right = Heap._move_up(node.right, value)
        if node.left:
            if node.left.value == value:
                new_parent = node.left.value
                new_left = node.value

                node.value = new_parent
                node.left.value = new_left

        if node.right:
            if node.right.value == value:
                new_parent = node.right.value
                new_right = node.value

                node.value = new_parent
                node.right.value = new_right

        return node

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.
        FIXME:
        Implement this function.
        '''
        for x in xs:
            self.insert(x)

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.
        FIXME:
        Implement this function.
        This function is not implemented in the lecture notes,
        HINT:
        Create a recursive staticmethod helper function,
        similar to how the insert and find functions have recursive helpers.
        '''
        if self.root:
            return Heap._find_smallest(self.root)

    @staticmethod
    def _find_smallest(node):
        return node.value

    def remove_min(self):
        '''
        Removes the minimum value from the Heap.
        If the heap is empty, it does nothing.
        FIXME:
        Implement this function.
        '''
        if self.root is None:
            return None
        elif self.root.left is None and self.root.right is None:
            self.root = None
        else:
            replace_right = Heap._find_right(self.root)
            self.root = Heap._remove(self.root)
            if replace_right == self.root.value:
                return
            else:
                self.root.value = replace_right
            if not Heap._is_heap_satisfied(self.root):
                return Heap._move_down(self.root)

    @staticmethod
    def _remove(node):
        '''
        '''
        if node is None:
            return
        elif node.right:
            node.right = Heap._remove(node.right)
        elif node.left:
            node.left = Heap._remove(node.left)
        else:
            if node.right is None and node.left is None:
                return None

        return node

    @staticmethod
    def _find_right(node):
        '''
        '''
        if node.left is None and node.right is None:
            return node.value
        elif node.right:
            return Heap._find_right(node.right)
        elif node.left:
            return Heap._find_right(node.left)

    @staticmethod
    def _move_down(node):
        '''
        '''
        left = node.left
        right = node.right

        if node.left is None and node.right is None:
            return node

        if left and (not right or left.value <= right.value):
            if node.left.value < node.value:
                new_parent = node.left.value
                new_left = node.value

                node.value = new_parent
                node.left.value = new_left

            node.left = Heap._move_down(node.left)

        elif right and (not left or right.value <= left.value):
            if node.right.value < node.value:
                new_parent = node.right.value
                new_right = node.value

                node.value = new_parent
                node.right.value = new_right

            node.right = Heap._move_down(node.right)
        return node
