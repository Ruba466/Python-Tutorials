print("\nIF-ELSE example:")
age = 17
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")




print("\nIF-ELIF-ELSE example:")
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")



print("\nFOR loop example:")
for i in range(1, 6):
    print("Number:", i)
    

print("\nFOR loop with CONTINUE:")
for i in range(1, 6):
    if i % 2 == 0:
        continue  
    print("Odd Number:", i)



print("\nWHILE loop example:")
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1



print("\nWHILE loop with BREAK:")
count = 1
while True:
    if count == 4:
        break  
    print("Current count:", count)
    count += 1



print("\nWHILE loop with ELSE:")
count = 1
while count <= 3:
    print("Count:", count)
    count += 1
else:
    print("Loop ended because condition is false.")


'''
IF-ELSE example:
You are not eligible to vote.

IF-ELIF-ELSE example:
Grade: B

FOR loop example:
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5

FOR loop with CONTINUE:
Odd Number: 1
Odd Number: 3
Odd Number: 5

WHILE loop example:
Count is: 1
Count is: 2
Count is: 3
Count is: 4
Count is: 5

WHILE loop with BREAK:
Current count: 1
Current count: 2
Current count: 3

WHILE loop with ELSE:
Count: 1
Count: 2
Count: 3
Loop ended because condition is false.

'''