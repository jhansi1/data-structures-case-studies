class Queue:
    # We use a basic list to implement a Queue data structure
    def __init__(self):
        self._queue = []

    # Return true if queue is empty
    def empty(self):
        if(len(self._queue) == 0):
            return True
        return False

    # Returns the length of the queue
    def size(self):
        return len(self._queue)

    # Enqueues an item to the end of the queue
    def enqueue(self, item):
        self._queue.append(item)

    # Dequeues an item from the front of the queue
    # It returns None if the queue is empty
    def dequeue(self):
        if(self.empty()):
            return None
        return self._queue.pop(0)

    # Returns the item at the front of the queue without removing it
    # Sometimes you need to peek at the value but not remove it from the queue yet
    # It returns None if the queue is empty
    def front(self):
        if (not self.empty()):
            return self._queue[0]
        else:
            return None

    # Returns the item at the rear of the queue without removing it
    # Sometimes you need to peek at the value but not remove it from the queue yet
    # It returns None if the queue is empty
    def rear(self):
        if(self.empty()):
            return None
        return self._queue[-1]
