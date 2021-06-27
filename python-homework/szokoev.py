# year_input = int(input("Enter a year, and I will tell you if it is a leap year: "))
# if year_input%4 == 0:
#     if year_input%100 == 0:
#         if year_input%400 == 0:
#             print("It is a leap year")
#         else:
#             print("It is not a leap year")
#     else:
#         print("It is a leap year")
# else:
#     print("It is not a leap year")


year_input = int(input("Enter a year, and I will tell you if it is a leap year: "))

def function(year_input):
    output = False
    if year_input%4 == 0:
        if year_input%100 == 0:
            if year_input%400 == 0:
                output = True
            else:
                output = False
        else:
            output = True
    else:
        output = False
    return output

if function(year_input) == True:
    print("It is a leap year")
else:
    print("It is not a leap year")