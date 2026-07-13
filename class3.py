#topics taught in c3; 1. use of len 2. lcase and ucase. 3.concatenation(merging two diff datatypes)
#4. keywordz = str, int, float. 5. " " used for spacing within prompts
user_name = str(input("Enter thy name "))
user_age = int(input("Enter thy age "))
user_city = str(input("Enter thy residential city "))
fav_person = str(input("Enter da luckeh person's name bro "))
last_name = str(input("Enter your last name ",))
full_name = user_name + " " + last_name
print("\nWelcome:", full_name, "| Type:", type(full_name) )
print("Your age:", user_age, "| Type:", type(user_age))
print("Your residential city:", user_city, "| Type:", type(user_city))
word_length = len(fav_person)
print("Mate yo username luks like dis in lowercase", full_name.lower())
print("Mate did yk ur name luks like dis in uppercase", full_name.upper())
print("Bet da word count of yo fav person's name's:", word_length)
print("You'll be", user_age + 1, "next year, unc lol")



