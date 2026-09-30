
class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        """
        TODO:
        - Assign the provided 'data' to an instance variable.
        - Initialize 'next' to None.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        """
        TODO:
        - Initialize 'head' to None to represent an empty list.
        """
        self.head = None

    def insert_at_front(self, data):
        """
        TODO:
        - Create a new Node with 'data'.
        - Insert it at the front of the list (head).
        - Update 'head' to the new node.
        """
        new_node =Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        (Optional) TODO:
        - Create a new Node with 'data'.
        - Traverse to the end of the list.
        - Set the last node's 'next' reference to the new node.
        """
        new_node =Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def recursive_sum(self):
        """
        TODO:
        - Use recursion to sum all node data in the list.
        - Consider a helper function that:
          1. Checks if the current node is None, and returns 0 if so.
          2. Otherwise, returns node.data + recursive call on node.next.
        - Return the total sum.
        """
        def sum_from(node):
            if node is None:
                return 0
            return node.data + sum_from(node.next)

        return sum_from(self.head)

    def recursive_search(self, node_or_target, target=None):
        """
        Returns True if 'target' is found, otherwise False, using recursion.
        Handles calls with 1 argument `recursive_search(target)` or 2 arguments `recursive_search(head, target)`.
        """
        if target is None:
            current = self.head
            search_target = node_or_target
        else:
            current = node_or_target
            search_target = target

        # Base case 1: reached end of list without finding target
        if current is None:
            return False

        # Base case 2: found target match
        if current.data == search_target:
            return True

        # Recursive case: search next node
        return self.recursive_search(current.next, search_target)

    def recursive_reverse(self, current=None, is_initial=True):
        """
        Reverses the list in-place using recursion and updates self.head.
        """
        if is_initial:
            self.head = self._reverse_helper(self.head, None)
            return self.head
        return self._reverse_helper(current, None)

    def _reverse_helper(self, current, prev):
        # Base case: reached end of list; return new head
        if current is None:
            return prev

        next_node = current.next
        current.next = prev

        # Recursive case: advance pointers
        return self._reverse_helper(next_node, current)

    def display(self):
        """
        Prints the contents of the list in 'val -> val -> None' format.
        """
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")