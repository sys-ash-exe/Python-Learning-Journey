score = int(input("Enter your score "))
clear = False
if score>=50:
    clear = True
    print("You passed")
    if score>=60 and clear == True:
            print("Grade: C")
    elif score>=70 and clear == True:
            print("Grade: B")
    elif score>=80 and clear == True:
            print("Grade: A")
    elif score>=90 and clear == True:
            print("Grade: A+")
else:
    print("You failed, retake the exam")