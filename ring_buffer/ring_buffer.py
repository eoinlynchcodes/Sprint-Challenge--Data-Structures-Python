class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def append(self, item):
        print(self.capacity)
        print(self.data)
        if [len(self.data)] == self.capacity:
            self.data.pop(0)
            self.data.reverse()
            self.data.append(item)
            self.data.reverse()
        else:
            self.data.append(item)

    def get(self):
        return self.data

test = RingBuffer(4)

test.get()
test.append('a')
test.append('b')
test.append('c')
test.get()
test.append('d')
test.append('e')
test.append('f')
test.get()