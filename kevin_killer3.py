class abc:
    def f():
        try:
            lst = [1,2,5,6]
            for i in range(9):
                print("Ans : ",lst[i])
        except:
                print("Out Of Rnage..!!")

    f()

    def g():
        try:
            print("Value : ",x)
        except:
            print("variable is not define..!")

    g()

m1 = abc()

m1.f()
m1.g()
