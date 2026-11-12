import random

def play(low: int = 1, high: int = 100, max_tries: int = 7) -> None:
    secret = random.randint(low, high)
    print(f"Guess the number between {low} and {high}. You have {max_tries} tries.")

    attempt = 1;
    while attempt <= max_tries:
        raw = input(f"Attempt {attempt}: ")
        if not raw.isdigit():
            print("Enter a whole number.")
            continue

        guess = int(raw)
        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"Correct! You got it in {attempt} tries.")
            return

        attempt = attempt + 1

    print(f"Out of tries. The number was {secret}.")



if __name__ == "__main__":
    while True:
        play()
        answer = input("play again? (y/n) ")
        if answer.lower() != "y":
            break
