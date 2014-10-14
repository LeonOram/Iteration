total = 0

for counter in range(5):
    number = int(input("Please enter number {0} in the series".format(counter+1)))
    total = total + number
    counter = counter + 1
print("The total of the numbers you entered is {0}".format(total))
