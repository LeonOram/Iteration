#Leon Oram
#30-10-2014
#SC Task 3

binary = input("Please enter a 8-bit binary number: ")
decimal = 0

for character in binary:
    bit = int(character)
    decimal = decimal * 2 + bit
print("{0}(Base 2) == {1}(Base 10)".format(binary,decimal))
