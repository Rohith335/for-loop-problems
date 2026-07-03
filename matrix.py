# 07. Write a Python script that uses nested for loops to print a 5x5 matrix of numbers from 1 to 25.
num = 1  

for i in range(5):  # outer loop for rows
    for j in range(5):  # inner loop for columns
        print(num, end="\t")  # print number with tab spacing
        num += 1  # move to next number
    print()  # new line after each row
