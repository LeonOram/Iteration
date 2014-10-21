#Leon Oram
#21-10-2014
#Dev Task 2

row_output = ""
per_row = int(input("Please enter the number of stars per row: "))
rows = int(input("Please enter the number of rows: "))

for count1 in range(per_row):
        row_output = row_output + "*"
for count2 in range(rows):
    print(row_output)
