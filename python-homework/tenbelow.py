list_of_inputs = []

user_input = 0

while True:
    user_input = int(input("Írj be egy számot, ami kisebb mint 10: "))
    if user_input >= 10:
        break
    list_of_inputs.append(user_input)

print(sum(list_of_inputs))


