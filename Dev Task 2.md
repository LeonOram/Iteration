OUTPUT Please enter the number of stars per row
per_row ← USERINPUT
OUTPUT Please enter the number of rows
rows ← USERINPUT
row_output ← 0
FOR count1 ← 1 TO rows
	FOR count2 ← 1 TO per_row
		row_output = row_output + "*"
	OUTPUT row_output