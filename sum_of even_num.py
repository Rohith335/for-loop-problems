# 03. Implement a for loop to find and print the sum of all even numbers in a given list of integers.
numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
count=0
for x in numbers:
    if x%2==0:
        count=count+x
print("sum of even numbers:", count)
