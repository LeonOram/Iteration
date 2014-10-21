#Leon Oram
#21-10-2014
#Dev Task 3
string_in = input("Please enter a string: ")
length = len(string_in)
string_out = ""
for index in range(length-1,-1,-1):
   string_out = string_out + string_in[index] 
print(string_out)
