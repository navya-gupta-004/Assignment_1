# Task 1: Calculate Factorial Using a Function 


def factorial(n):
    if n == 1 :
        return 1
    else:
        return n * factorial(n-1)

#method2 using loop

def factorial(n):
    fact =1
    for i in range(n):
        fact = fact * (i+1)
    return fact

    
num = int(input("enter a number :"))
result = factorial(num)
print(f"factorial of {num} is {result}")

# task-2

import math

num=int(input("enter a number:  "))

out = math.sqrt(num)
print("square root",out)

res1=math.sin(num)
print("sin",res1)

res2=math.log(num)

print("logarithm",res2)

