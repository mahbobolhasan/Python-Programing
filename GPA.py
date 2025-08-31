GPA = int(input("Enter your GPA="))
if GPA>=80 and GPA<=100:
    print("A+")
elif GPA>=70 and GPA<80:
    print("A")
elif GPA>=60 and GPA<70:
    print("A-")
elif GPA>=50 and GPA<60:
    print("B")
elif GPA>=40 and GPA<50:
    print("C")
elif GPA>=33 and GPA<40:
    print("D")
else:
    print("Sorry! You are fail")