#creating a login page
pass_saved = "yamitakudasai"
user_saved = "ashire_08"
choice = input("Would you like to login or signup: ").lower()
user_age = int(input("Enter age: "))
if choice == "signup" and user_age>=18:
    signup = True
    if signup == True:
        user_name  = input("Write the uername you'd like to set: ")
        pass_input = input("Enter the password you'd like to set: ")
        pass_check = input("Re-enter your set password:")
        if pass_input==pass_check:
            print("password is set")
        else:
            pass_check = input("Incorrect, re-enter: ")
    else:
        choice = input("Enter login to proceed: ")
elif choice == "login" and user_age>=18:
    acc_login = True
    if acc_login== True:
        user_name = input("Enter your username: ")
        pass_input = input("Enter your password: ")
        if user_name==user_saved and pass_input==pass_saved:
            print("Login successful")
        else:
            print("Incorrect username or password")
elif user_age>=18:
    print("You need to enter either login or signup to proceed")
else:
    print("You are not old enough to proceed")

        


