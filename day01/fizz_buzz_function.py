def fizz_buzz(num:int) -> list[str | int]:
    return [
        "Fizz Buzz" if x % 15 == 0 else
        "Fizz" if x % 3 == 0 else
        "Buzz" if x % 5 == 0 else
        x
        for x in range(1, num + 1)
    ]

def main():
    raw = input("enter limit ")
    if not raw.isdigit():
        print("Enter a whole number.")
    else:
        limit = int(raw)
        print(fizz_buzz(limit))



if __name__ == '__main__':
    main()
