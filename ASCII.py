#Leon Oram
#06-10-2014
#ASCII task 1

ascii_code = int(input("Please enter your ASCII code: "))
text_chara = input("Please enter a text character: ")

ascii_chara = chr(ascii_code)
text_code = ord(text_chara)

print("That ASCII code is :{0} That text's code is:{1}".format(ascii_chara,text_code))
