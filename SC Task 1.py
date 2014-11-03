#Leon Oram
#28-10-2014
#SC Task 1
square_print=""
max_number = int(input("Please enter a number: "))

for count in range(1,max_number+1):
    square_int = count ** 2
    square_string = str(square_int)
    square_print = square_print+" "+square_string
print(square_print)
