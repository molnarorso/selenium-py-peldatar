user_age = input("your age? ")
drink_chosen = input("beer or coke? ")
if int(user_age) < 18:
    if drink_chosen == "beer":
        print("sorry, you are not allowed to have a beer")
    elif drink_chosen == "coke":
        print("here is your coke")
    else:
        print("we only have beer and coke")
elif int(user_age) > 60:
    if drink_chosen == "coke":
        print("caffeine may elevate your blood pressure")
    elif drink_chosen == "beer":
        print("here is your beer")
    else:
        print("we only have beer and coke")
elif 18 <= int(user_age) <= 60:
    if drink_chosen == "beer":
        print("here is your beer")
    elif drink_chosen == "coke":
        print("here is your coke")
    else:
        print("we only have beer and coke")
