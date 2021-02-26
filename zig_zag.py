class ZigZag:
    def __init__(self,l1,l2):
        self.queue=[l1,l2]

    def next(self):
        v=self.queue.pop(0)
        r=v.pop(0)
        if v:  
            self.queue.append(v)
        return r

    def finish(self):
        if self.queue:
            return True
        return False
        

a=ZigZag([1,3,5,7,9],[2,4,6,8,10])
while a.finish():
    print(a.next(),end=' ')