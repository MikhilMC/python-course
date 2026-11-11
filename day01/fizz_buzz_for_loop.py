def fizz_buzz(limit:int = 20) -> None:
    for value in range(1, limit + 1):
        if value % 15 == 0:
            print("Fizz Buzz")
        elif value % 3 == 0:
            print("Fizz")
        elif value % 5 == 0:
            print("Buzz")
        else:
            print(value)


if __name__ == '__main__':
    raw = input("enter limit ")
    if not raw.isdigit():
        print("Enter a whole number.")
    else:
        limit = int(raw)
        fizz_buzz(limit)
