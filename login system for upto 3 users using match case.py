#building a login system with atleast 3 usernamez
user_name1 = "hamdan_gay"
user_name2 = "john_doe"
user_name3 = "jane_smith"
pass_w = "bazooka08"
input_user = input("Enter your username: ")
match input_user:
    case "hamdan_gay":
        print("Welcome hamdan_gay")
        in_pass = input("Enter your password: ")
        if in_pass == pass_w:
            print("Access granted")
        else:
            print("Access denied")
    case "john_doe":
        print("Welcome john_doe")
        in_pass = input("Enter your password: ")
        if in_pass == pass_w:
            print("Access granted")
        else:
            print("Access denied")
    case "jane_smith":
        print("Welcome jane_smith")
        in_pass = input("Enter your password: ")
        if in_pass == pass_w:
            print("Access granted")
        else:
            print("Access denied")
    case _:
        print("Username not recognized")