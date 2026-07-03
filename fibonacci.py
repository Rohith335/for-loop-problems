# 05. Solve the "Fibonacci sequence" problem by generating the first 10 numbers in the sequence using a for loop.
a, b = 0,1
print("first 10 Fibonacci numbers: ")
for i in range(10):
    print(a,end="")
    a,b=b,a+b



