class Node:
    def __init__(self, task):
        self.task = task
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_task(self, task):
        new_node = Node(task)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_task(self, task):
        if not self.head:
            return

        if self.head.task == task:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.task == task:
                current.next = current.next.next
                if not current.next:
                    self.tail = current  # Update tail if needed
                return
            current = current.next

    def get_tasks(self):
        tasks = []
        current = self.head
        while current:
            tasks.append(current.task)
            current = current.next
        return tasks

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, task):
        self.items.append(task)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def get_tasks(self):
        return self.items