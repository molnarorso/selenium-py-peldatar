list_of_inputs = []

user_input = 1

while True:
    user_input = int(input("Enter a positive number: "))
    if user_input == 0:
        break
    list_of_inputs.append(user_input)
list_of_inputs.reverse()
print(list_of_inputs)