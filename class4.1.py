integer = int(input("Enter a number "))
name = str(input("Enter your name "))
if integer>=0:
    print(name.upper()+","+" "+ "Your integer is positive")
elif integer<0:
    print(name.upper()+","+" "+ "Your integer is negative")
else:
    print("Invalid Output")