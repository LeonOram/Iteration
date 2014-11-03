#Leon Oram
#30-10-2014
#SC Task 2

binary = ""

denary = int(input("Please enter a denary number: "))
remainder = denary
if denary <= 255 and denary >= 0 :
    for count in range(8):
        bit = remainder % 2
        bit = str(bit)
        binary = bit + binary
        remainder = remainder // 2
    print("{0}(Base 10)=={1}(Base 2)".format(denary,binary))
else:
    print("That is not a valid number for 8 bits ")

