name = input("Enter your name ")
marks = int(input("Enter your marks "))
if marks >= 90:
    print("Student Name:"+ " " + name + "Grade: A*")
elif marks >= 80:
    print("Student Name:"+ " " + name + " " + "Grade: A")
elif marks >= 70:
    print("Student Name:"+ " " + name + " " + "Grade: B")
elif marks >=60:
    print("Student Name:"+ " " + name + " " + "Grade: C")
elif marks >=50:
    print("Student Name:"+ " " + name + " " + "Grade: U(Fail)")
else:
    print("Invalid Input")



