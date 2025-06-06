# Python Operators Demo with User Input

# Taking input from the user
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))

print("\n---- Arithmetic Operators ----")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b if b != 0 else "undefined (division by zero)")
print("a % b =", a % b if b != 0 else "undefined (mod by zero)")
print("a ** b =", a ** b)
print("a // b =", a // b if b != 0 else "undefined (floor division by zero)")

print("\n---- Assignment Operators ----")
x = a
print("x =", x)
x += b
print("x += b ->", x)
x -= b
print("x -= b ->", x)
x *= b
print("x *= b ->", x)
x /= b if b != 0 else 1
print("x /= b ->", x)
x %= b if b != 0 else 1
print("x %= b ->", x)
x //= b if b != 0 else 1
print("x //= b ->", x)
x **= b
print("x **= b ->", x)

print("\n---- Comparison Operators ----")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\n---- Logical Operators ----")
print("a > 0 and b > 0:", a > 0 and b > 0)
print("a > 0 or b > 0:", a > 0 or b > 0)
print("not(a > 0):", not(a > 0))

print("\n---- Bitwise Operators ----")
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~a:", ~a)
print("a << 1:", a << 1)
print("a >> 1:", a >> 1)

print("\n---- Membership Operators ----")
sample_list = [1, 2, 3, a, b]
print(f"{a} in sample_list:", a in sample_list)
print(f"{b} not in sample_list:", b not in sample_list)

print("\n---- Identity Operators ----")
x = [a, b]
y = [a, b]
z = x
print("x is z:", x is z)
print("x is y:", x is y)
print("x == y:", x == y)
print("x is not y:", x is not y)

