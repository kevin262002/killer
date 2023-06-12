try:
    s1 = int(input("Enter marks of Gujrati : "))
    s2 = int(input("Enter marks of English : "))
    s3 = int(input("Enter marks of Stat : "))
    s4 = int(input("Enter marks of Account : "))
    s5 = int(input("Enter marks of Economic : "))

    if s1>=100 or s2>=100 or s3>=100 or s4>=100 or s5>=100:
        raise ValueError
    else:
        marks = s1+s2+s3+s4+s5
        print("Total Marks : ",marks)
        avg = marks/5
        print("Average : ",avg)

except ValueError:
    print("Error...!, Please Enter Valid Marks...")

    

    
