def compute(num:int) -> str | int:
    if num % 15 == 0:
        return "Fizz Buzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def fizz_buzz(num:int) -> list[str | int]:
    return [compute(x) for x in range(1, num + 1)]

def main():
    raw = input("enter limit ")
    if not raw.isdigit():
        print("Enter a whole number.")
    else:
        limit = int(raw)
        print(fizz_buzz(limit))



if __name__ == '__main__':
    main()
