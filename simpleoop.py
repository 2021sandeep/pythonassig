class calculater:
    a=0
    b=0
    def __int__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print("first value:",self.a)
        print("second value:",self.b)
        print("adition of two numbers:",self.ans)
   # def addition(self):
        #self.ans=self.a+self.b
obj=calculater()
#obj.addition("100","100")
obj.display(100,100)

