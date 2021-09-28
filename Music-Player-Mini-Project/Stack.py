class Stack:
    # We use a basic list to implement a Stack data structure
    def __init__(self):
        self._stack = []

    # Returns true if the stack is empty
    def empty(self):
        if(len(self._stack) == 0):
            return True
        return False

    # Returns the length of the stack
    def size(self):
        return len(self._stack)

    # Pushes elements on the stack by appending to the end of the list
    def push(self, item):
        self._stack.append(item)

    # Removes the last items in the list, and returns it.
    # It returns None if the stack is empty
    def pop(self):
        if(self.empty()):
            return None
        return self._stack.pop()

    # Returns the top of stack without removing it from the stack
    # Sometimes you need to peek at the value but not remove it from the stack yet
    # It returns None if the stack is empty
    def peek(self):
        if (not self.empty()):
            return self._stack[-1]
        else:
            return None