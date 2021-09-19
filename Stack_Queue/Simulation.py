"""TODO_: Please add some more commands to complete the code
"""

import random as rd


class Node:
    # to init a new Node with given value
    def __init__(self, value):
        self.data = value
        self.next = None


# class Queue to represent the queue of customers waiting
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    '''
        Đây là phần đoạn code mà cô viết, em nghĩ là nó bị sai ở chỗ self.next ạ
        def enqueue(self, value):
        newNode = Node(value)
        self.next = newNode
        if self.isEmpty():
            self.head = newNode
        self.size += 1
        self.tail = newNode 
        '''
    def enqueue(self, data):
        newNode = Node(data)
        if self.isEmpty() :
            self.head = self.tail = newNode
            self.size += 1
            return
        self.tail.next = newNode
        self.tail = newNode
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print("The queue is empty.")
            return
        tmp = self.head
        self.head = tmp.next
        self.size -= 1
        return tmp.data

    # class Customer to represent a customer. Can add more information


class Customer:
    def __init__(self, idNumber, arrivalTime):
        self.id = idNumber
        self.arrivalTime = arrivalTime


# class Counter, to represent a counter.
class Counter:
    def __init__(self, idNumber):
        self.id = idNumber
        self.nCustomer = 0
        self.stopTime = -1
        self.customer = None

    def isFree(self):
        return self.customer is None

    # A counter starts serving a customer at a given time
    def startServe(self, customer, stopTime):
        self.customer = customer
        self.stopTime = stopTime

    # A counter stop serving a customer
    def stopServe(self):
        self.nCustomer += 1
        cur = self.customer
        self.customer = None
        return cur

    # check if a counter finishs serving current customer at a given time.
    def isFinished(self, curTime):
        return self.stopTime == curTime and self.customer is not None


# class Simulation to simulate the system
class Simulation:
    def __init__(self, nCounter, betweenTime, minTime , maxTime , simulationTime):
        self.nCounter = nCounter
        self.betweenTime = betweenTime
        #self.serviceTime = serviceTime
        self.minTime = minTime
        self.maxTime = maxTime
        self.sTime = simulationTime
        self.customerQueue = Queue()
        self.totalWaitTime = 0
        self.nCustomer = 0

        self.counters = [None] * nCounter
        for i in range(nCounter):
            self.counters[i] = Counter(i + 1)

        #: This function checks if a new customer arrives at a given time. If yes, enqueue him.

    def handleArrival(self, curTime):
        p = rd.randint(1, self.betweenTime)
        # if p==1 then a new customer is coming
        if p == 1:
            # TODO_
            self.nCustomer +=1
            curCustomer = Customer(self.nCustomer, curTime)
            self.customerQueue.enqueue(curCustomer)
            print("Time {}: customer {} arrived.".format(curTime, curCustomer.id))

    # This function checks each counter, if it is free and if there is a customer waiting,2 then the customer will be served by this counter
    def handleBeginService(self, curTime):
        for counter in self.counters:
            if counter.isFree() and not self.customerQueue.isEmpty():
                # TODO_
                curCustomer = self.customerQueue.dequeue()
                self.totalWaitTime += curTime - curCustomer.arrivalTime
                counter.startServe(curCustomer, curTime + rd.randint(self.minTime ,self.maxTime))
                print("Time {}: counter {} starts serving customer {}.".format(curTime, counter.id, curCustomer.id))

    # This function checks each counter, if the estimated stop time == curTime, then free the counter
    def handleEndService(self, curTime):
        for counter in self.counters:
            if counter.isFinished(curTime):
                # TODO_:
                curCustomer = counter.stopServe()
                print("Time {}: counter {} stops serving customer {}. ".format(curTime, counter.id, curCustomer.id))

    def run(self):
        print("The system starts working.")
        for iTime in range(self.sTime):
            self.handleArrival(iTime)
            self.handleBeginService(iTime)
            self.handleEndService(iTime)
        print("The system stops working.")

    # TODO_: complete this function to print the number of customers still waiting at the end of the day.
    def report(self)        :
         print("The queue has {} customers waiting".format(self.customerQueue.size))
    def averageWaitTime(self):
        print('The average waiting time: {}'.format(self.totalWaitTime /(self.nCustomer - self.customerQueue.size)))

#########################
nCounts = int(input('Number of counters: '))
sTime = int(input('Simulation time number: '))
minTime = int(input("Input minximum service time: "))
maxTime = int(input('Input maximum service time: '))
s = Simulation(nCounts, 3 ,minTime, maxTime, sTime)
s.run()
s.report()
s.averageWaitTime()
