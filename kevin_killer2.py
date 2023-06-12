class abc(Exception):
 
    def __init__(self, sal,msg="Salary is not range in 15000 up..!!"):
        self.sal = sal
        self.msg=msg
        print("salary is :=",self.sal)
        super().__init__(self.msg)


sal= int(input("Enter salary amount: "))

if sal<=15000:
    raise abc(sal)
else:
    print("salary is :=",sal)
