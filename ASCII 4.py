#Leon Oram
#10-10-2014
#ASCII Task 4
import pdb

pdb.set_trace()

binary = input("Please enter a 7-bit binary string: ")

ones = 0
for counter in range(8):
    diget = binary[counter:counter+1]
    if diget =="1":
        ones = ones + 1
if ones % 2 == 0: #Even
    parity = "1"
elif ones % 2 == 1: #Odd
    parity = "0"

print("With odd parity that is {0}{1}".format(parity,binary))
