class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def add(self, x):
        new_node = Node(x)
        if self.last is None:
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return (" Coada este goala ")
        val = self.first.data
        self.first = self.first.next
        self.size -= 1
        return val

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def Size(self):
        return self.size

    def __repr__(self):
        coada = []
        curr = self.first
        while curr:
            coada.append(curr.data)
            curr = curr.next
        return repr(coada)

# am bagat si astea din VS sa vad ca merg dar e ok si asa 
my_queue = Queue()

my_queue.add(1)
my_queue.add(2)
my_queue.add(3)
my_queue.add(5)
my_queue.add(12)
my_queue.pop()


print("Queue:", my_queue) 
print("Pop:", my_queue.pop())  
print("Is Empty:", my_queue.isEmpty())  
print("Size:", my_queue.Size())  
print("Queue:", my_queue)  
