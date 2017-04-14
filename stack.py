#!/usr/bin/env python
"""Basic search algorithms."""


class LinkedList(object):
    """A linked list."""

    def __init__(self, data, next_):
        self.data = data
        self.next_ = next_


class Stack(object):
    """A simple stack data type."""

    def __init__(self):
        self.list = None
        self._sum = 0
        self.count = 0

    def __iter__(self):
        """Iterate down the stack."""
        node = self.list
        while node:
            yield node.data
            node = node.next_

    def copy(self):
        """Duplicate the stack."""
        new_stack = Stack()
        if not self.list:
            return new_stack
        new_stack.push(self.tip())
        new_node = new_stack.list
        node = self.list
        while node.next_:
            node = node.next_
            new_node.next_ = LinkedList(node.data, None)
            new_node = new_node.next_
            new_stack._sum += node.data
            new_stack.count += 1
        return new_stack

    def push(self, data):
        """Push to the top of the stack."""
        self.list = LinkedList(data, self.list)
        self._sum += data
        self.count += 1

    def pop(self):
        node = self.list
        if not node:
            return node
        self.list = node.next_
        self._sum -= node.data
        self.count -= 1
        return node.data

    def tip(self):
        try:
            return self.list.data
        except AttributeError:
            return None

    def sum(self):
        return self._sum

    def average(self):
        try:
            return self._sum / float(self.count)
        except ZeroDivisionError:
            return 0

    def max(self):
        node = self.list
        if not node:
            return node
        maximum = node.data
        while node:
            if node.data > maximum:
                maximum = node.data
            node = node.next_
        return maximum

    def prune_highest(self):
        if not self.list:
            return None
        highest_prev = None
        highest = self.list

        node = self.list
        while node.next_:
            prev = node
            node = node.next_
            if node.data > highest.data:
                highest_prev = prev
                highest = node
        if not highest_prev:
            return self.pop()  # Loop didn't execute, single-item list.

        node = highest
        highest_prev.next_ = node.next_
        self.count -= 1
        self._sum -= node.data
        return node.data


def verify(stack, tip, sum_, average, max_, list_, highest, list_no_highest):
    assert stack.tip() == tip
    assert stack.sum() == sum_
    assert stack.average() == average
    assert stack.max() == max_
    assert list(stack) == list_

    stack = stack.copy()
    assert stack.tip() == tip
    assert stack.sum() == sum_
    assert stack.average() == average
    assert stack.max() == max_
    assert list(stack) == list_

    assert stack.prune_highest() == highest
    assert list(stack) == list_no_highest


def main():
    """Main function."""
    # Empty.
    stack = Stack()
    verify(stack, None, 0, 0, None, [], None, [])
    assert stack.pop() is None
    verify(stack, None, 0, 0, None, [], None, [])

    # One.
    stack.push(12)
    verify(stack, 12, 12, 12, 12, [12], 12, [])

    # Two.
    stack.push(6)
    verify(stack, 6, 18, 9, 12, [6, 12], 12, [6])

    # Three.
    stack.push(3)
    verify(stack, 3, 21, 7, 12, [3, 6, 12], 12, [3, 6])

    # Four.
    stack.push(100)
    verify(stack, 100, 121, 30.25, 100, [100, 3, 6, 12], 100, [3, 6, 12])

    # Three.
    assert stack.pop() == 100
    verify(stack, 3, 21, 7, 12, [3, 6, 12], 12, [3, 6])

    # Four.
    stack.push(-1)
    verify(stack, -1, 20, 5, 12, [-1, 3, 6, 12], 12, [-1, 3, 6])

    # Eight.
    stack.push(10)
    stack.push(30)
    stack.push(0)
    stack.push(20)
    verify(stack, 20, 80, 10, 30, [20, 0, 30, 10, -1, 3, 6, 12], 30, [20, 0, 10, -1, 3, 6, 12])


if __name__ == '__main__':
    main()
