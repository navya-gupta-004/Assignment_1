# Task 1: Check if a Number is Even or Odd
num = int(input("Enter a number: "))

if num%2 == 0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")
    

# Task 2: Sum of Integers from 1 to 50 Using a Loop

sum = 0

for i in range(1,51):
    sum =sum + i
print(f"sum of interger from 1 to 50 is: {sum}")