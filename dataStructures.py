import heapq

class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_node = self.Node(task)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_task(self, task):
        if not self.head:
            return False
        if self.head.data[0] == task:
            self.head = self.head.next
            return True
        current = self.head
        while current.next and current.next.data[0] != task:
            current = current.next
        if current.next:
            current.next = current.next.next
            return True
        return False

    def get_tasks(self):
        tasks = []
        current = self.head
        while current:
            tasks.append(current.data)
            current = current.next
        return tasks


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        heapq.heappush(self.queue, item)  

    def dequeue(self):
        if self.queue:
            return heapq.heappop(self.queue)
        return None

    def remove_task(self, task):
        self.queue = [item for item in self.queue if item[1] != task]
        heapq.heapify(self.queue)  

    def get_tasks(self):
        return sorted(self.queue)  
