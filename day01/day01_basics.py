# Variables and types (dynamic, but strongly typed)
name = "Mikhil"
age = 33
height = 5.9
is_dev = True
nothing = None

print(f"{name} is {age}, type of age: {type(age).__name__}")

# Strings
s = "  Hello, Python  "
print(s.strip().lower().replace("python", "django"))
print(s.strip().split(","))          # ['Hello', ' Python']
print("py" in s.lower())             # True

# Truthiness: empty/zero/None are falsy
for value in [0, "", [], None, "0", [0]]:
    print(repr(value), "->", bool(value))

# Control flow
score = 82
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print(grade)

# Loops
for i in range(1, 6):
    print(i, end=" ")
print()

for index, ch in enumerate("abc"):
    print(index, ch)

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print("n =", n)

# Gotchas worth knowing now
print(10 / 3)     # 3.333... (true division)
print(10 // 3)    # 3 (floor division)
print(-7 // 2)    # -4 (floors, doesn't truncate)
print(2 ** 10)    # 1024
print(0.1 + 0.2 == 0.3)  # False (floating point)
