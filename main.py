import random

class Queue:
  '''Represents a line. FIFO 
  
  Parameters: 
  init : takes self 
  isempty: takes self 
  enqueue: takes self and item
  dequeue: takes self
  size: takes self
  
  Returns:
  isempty: checks the list is empty or not 
  dequeue: pops the item from the list
  size: gives the length of the items list
  '''
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def enqueue(self, item):
    self.items.insert(0,item)

  def dequeue(self):
    return self.items.pop()

  def size(self):
    return len(self.items)

class Printer:
  '''represents a printer. Has a timer to see how long the printing is taking. Has a function to see if the printer is busy or not. Function to see what comes up in the queue to be printed. 
  
  Parameters:
  init: takes ppm(page per minute) and self
  tick: takes self
  busy: takes self
  startnext: self and newtask
  
  Returns:
  busy: returns true if currenttask is not none else false
  '''
  def __init__(self, ppm):
    self.pagerate = ppm
    self.currentTask = None
    self.timeRemaining = 0

  def tick(self):
    if self.currentTask != None:
      self.timeRemaining = self.timeRemaining - 1
      if self.timeRemaining <= 0:
        self.currentTask = None

  def busy(self):
    if self.currentTask != None:
      return True
    else:
      return False

  def startNext(self,newtask):
    self.currentTask = newtask
    self.timeRemaining = newtask.getPages() * 60/self.pagerate

class Task:
  '''gets timestamp when the printing began. getpages gets how many pages to print. waittime is how long it is going to take to print the pages.
  
  Parameters:
  init: takes self and time
  getstamp: takes self
  getpages: takes self
  waittime: takes self and currenttime
  
  Return:
  getstamp: returns the time the printing began
  getpages: returns the number of pages that are going to be printed
  waittime: returns the time the printing is going to take
  '''
  def __init__(self,time):
    self.timestamp = time
    self.pages = random.randrange(1,21)

  def getStamp(self):
    return self.timestamp

  def getPages(self):
    return self.pages

  def waitTime(self, currenttime):
    return currenttime - self.timestamp

def simulation(numSeconds, pagesPerMinute):
  '''Here pages are being added to the queue and the printer is moving onto another page if the printer is idle. It is also counting the time it takes for every page to print.
  
  Parameters: 
  simulation: is taking numseconds and pagesperminute
  '''
  labprinter = Printer(pagesPerMinute)
  printQueue = Queue()
  waitingtimes = []

  for currentSecond in range(numSeconds):
    if newPrintTask():
      task = Task(currentSecond)
      printQueue.enqueue(task)
    if (not labprinter.busy()) and (not printQueue.isEmpty()):
      nexttask = printQueue.dequeue()
      waitingtimes.append(nexttask.waitTime(currentSecond))
      labprinter.startNext(nexttask)

    labprinter.tick()

  averageWait=sum(waitingtimes)/len(waitingtimes)
  print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

def newPrintTask():
  '''Represents the task being created as a boolen True or False
  and a task is created every 180 seconds. The for i in range is running the simulation ten times and the time set for all the printing is set to 3600 at the printing speed of five.
  
  Return:
  True if the randomly generated number between 1 to 181(num) equals 180 else False 
  '''
  num = random.randrange(1,181)
  if num == 180:
    return True
  else:
    return False

for i in range(10):
  simulation(3600,5)