number = int(input("choose a number:"))

for i in range (number + 1): #We use number + 1 in the range to include the number chosen by the user
    if i % 3 == 0 or i % 5 == 0: #we check if the number is divisble by 3 and 5 using the % remainder operator
        print(i)