

class recur ():
    def __init__(self):
        self.callCount = 0
   
    def call(self):
        self.callCount +=1
        print(self.callCount)
        self.call()


recurInstance =recur()
recurInstance.call()