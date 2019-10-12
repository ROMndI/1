class Queue:
    def __init__(self):
        self.items = [schinfo,vinfo,kinfo]

    def is_empty(self):
        return self.items == []

    def enqueue(self):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)



class Queuev:
    def Queue.__init__(self):
        self.items = [vinfo]

    def is_empty(self):
        return self.items == []

    def enqueue(self):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)



class Queuesch(Queue):
    def Queue.__init__(self):
        self.items = [schinfo]

    def is_empty(self):
        return self.items == []

    def enqueue(self):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

a_queue = Queue()

print(a_queue.is_empty())

vop = input("вам куда: ")
if vop == schinfo:
    print("вы первый в schinfo: ")
elif vop == vinfo:
    print("вы первый в vinfo: ")
elif vop == kinfo:
    print("вы первый в kinfo: ")

queue = Queue()


