#Leon Oram
#10-10-2014
#ASCII Task 3

binary = input("Please enter your binary string: ")

ones = 0
for counter in range(8):
    diget = binary[counter:counter+1]
    if diget =="1":
        ones = ones + 1

if ones % 2 == 0:
    print("Valid")
else:
    print("Invalid")
