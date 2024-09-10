class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def calc_add(self):
        return self.num1+self.num2
    
    def calc_sub(self):
        return self.num1-self.num2
    
    def calc_mul(self):
        return self.num1*self.num2

    def calc_div(self):
        return self.num1/self.num2

if __name__=="__main__":
    print("hi")
