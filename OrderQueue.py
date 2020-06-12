from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder

class QueueEmptyException(Exception):
    pass

class OrderQueue:
    def __init__(self):
        self.heap = []
        self.size = 0

    def getSize(self):
        return self.size

    def parent(self, index): 
        return index // 2

    def addOrder(self,pizzaOrder):
        self.size = self.size + 1
        self.heap.append(pizzaOrder)
        if self.size == 1:
            return
        currentIndex = self.size - 1
        while self.heap[currentIndex].time < self.heap[self.parent(currentIndex)].time:
            self.heap[currentIndex], self.heap[self.parent(currentIndex)] = self.heap[self.parent(currentIndex)], self.heap[currentIndex]  #swap
            currentIndex = self.parent(currentIndex)

    def left(self, index): 
        return (2 * index) + 1

    def right(self, index): 
        return (2 * index) + 2

    def isLeaf(self, index): 
        if index >= (self.size//2) and index <= (self.size - 1): 
            return True
        return False

    def heapify(self, index): 
        if not self.isLeaf(index): 
            if self.right(index) < self.size:
                if (self.heap[index].time > self.heap[self.left(index)].time or self.heap[index].time > self.heap[self.right(index)].time): 
                    if self.heap[self.left(index)].time < self.heap[self.right(index)].time: 
                        self.heap[index], self.heap[self.left(index)] = self.heap[self.left(index)], self.heap[index]
                        self.heapify(self.left(index)) 
                    else: 
                        self.heap[index], self.heap[self.right(index)] = self.heap[self.right(index)], self.heap[index]
                        self.heapify(self.right(index)) 
            else:
                if self.heap[index].time > self.heap[self.left(index)].time: 
                    self.heap[index], self.heap[self.left(index)] = self.heap[self.left(index)], self.heap[index]
                    self.heapify(self.left(index)) 

    def processNextOrder(self):
        if self.size == 0:
            raise QueueEmptyException
        else:
            popped = self.heap[0]
            self.size = self.size - 1
            self.heap[0] = self.heap[self.size]
            self.heapify(0)
            return popped

# if __name__ == "__main__":
#     queue = OrderQueue()
#     order = PizzaOrder(1200)
#     order2 = PizzaOrder(1500)
#     order3 = PizzaOrder(1300)
#     order4 = PizzaOrder(1400)
#     queue.addOrder(order)
#     queue.addOrder(order2)
#     queue.addOrder(order3)
#     queue.addOrder(order4)
#     processed = queue.processNextOrder()
#     print(processed)
#     print(processed.getOrderDescription())
