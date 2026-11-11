def fizz_buzz(num:int) -> str | int:
    if num % 15 == 0:
        return "Fizz Buzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def main():
    raw = input("enter limit ")
    if not raw.isdigit():
        print("Enter a whole number.")
    else:
        limit = int(raw)
        result = [fizz_buzz(x) for x in range(1, limit + 1)]
        for value in result:
            print(value)



if __name__ == '__main__':
    main()
