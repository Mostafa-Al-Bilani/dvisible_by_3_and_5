number = int(input("choose a number:"))
numbers_divisble = []

for i in range (1, number + 1): #We use number + 1 in the range to include the number chosen by the user
    if i % 3 == 0 or i % 5 == 0: #we check if the number is divisble by 3 and 5 using the % remainder operator
        numbers_divisble.append(i)

print("The numbers divisble by 3 and 5 are:", numbers_divisble)
