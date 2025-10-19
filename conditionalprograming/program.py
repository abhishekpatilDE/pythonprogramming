#Creating conditional statements and looping constructs

## If staement, we print something based on condition
num = 10
if num > 0:
    print(f"{num} is a positive number.")
else:
    print(f"{num} is not a positive number.")   
    
## Elif statement, we print something based on multiple conditions
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")
## For loop, we iterate over a list and print each element
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

## While loop, we print numbers from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1
    
## Nested loops, we print a multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i * j}")
    print("-----")
    
## Loop with break and continue
for i in range(1, 10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break
    if i % 2 == 0:
        print("Skipping even number:", i)
        continue
    print("Current number:", i)
    
## Using pass statement in a loop
for i in range(1, 6):
    if i == 3:
        pass
    print("Current number:", i)
    
## Using else with loops
for i in range(1, 4):
    print("Iteration:", i)
else:
    print("Loop completed successfully.")
    
## Using nested if statements
num = 15
if num > 0:
    if num % 2 == 0:
        print(f"{num} is a positive even number.")
    else:
        print(f"{num} is a positive odd number.")
else:
    print(f"{num} is not a positive number.")       
    
## Using conditional expressions (ternary operator)
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")  


