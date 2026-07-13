fav_day = input("Enter your day: ").upper()
age = int(input("Enter your age: "))
match fav_day:
    case "MONDAY":
        if age>=18:
            eligible=True
            print(f"Favorite Day: {fav_day}| Age: {age}")
        else:
            print("Not old enough kiddo")
    case "TUESDAY":
        if age>=18:
            eligible=True
            print(f"Favorite Day: {fav_day}| Age: {age}")
        else:
            print("Not old enough kiddo")
    case "WEDNESDAY":
        if age>=18:
            eligible=True
            print(f"Favorite Day: {fav_day}| Age: {age}")
        else:
            print("Not old enough kiddo")
    case "THURSDAY":
        if age>=18:
            eligible=True
            print(f"Favorite Day: {fav_day}| Age: {age}")
        else:
            print("Not old enough kiddo")
    case "FRIDAY":
        if age>=18:
            eligible=True
            print(f"Favorite Day: {fav_day}| Age: {age}")
        else:
            print("Not old enough kiddo")
    case "SATURDAY":
        if age>=18:
            eligible=True
            print(f"Favorite Day: {fav_day}| Age: {age}")
        else:
            print("Not old enough kiddo")
    case "SUNDAY":
        if age>=18:
            eligible=True
            print(f"Favorite Day: {fav_day}| Age: {age}")
        else:
            print("Not old enough kiddo")
    case _:
        print("Invalid Day")
            
            
                       
            
            