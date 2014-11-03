#Leon Oram
#02-11-2014
#SC Task 4

string = input("Please enter a string: ")
words = 0
is_word = False
for character in string:
    if character == " " and is_word == True:
        words = words + 1
        is_word = False
    else:
        is_word = True
if words > 0 and character != " ":
    words = words + 1
print(words)
