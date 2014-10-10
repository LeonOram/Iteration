#Leon Oram
#06-10-2014
#ASCII task 2

import random

length = int(input("Please enter the length of your wanted password: "))
password = ""
for counter in range(length):
    c_l_n = random.randint(1,3)
    if c_l_n == 1: #Caps
        ascii_code = random.randint(65,90)
    elif c_l_n == 2: #lower case
        ascii_code = random.randint(97,122)
    elif c_l_n == 3: #number
        ascii_code = random.randint(48,57)
    chara = chr(ascii_code)
    password = password + chara
print("Your password is:{0}".format(password))
