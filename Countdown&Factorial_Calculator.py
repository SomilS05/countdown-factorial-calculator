from math import factorial


MAX_INPUT = 1000


def countdown(n):
    """Print the integers from n down to 1, followed by liftoff."""
    for number in range(n, 0, -1):
        print(number)
    print("Blastoff!")


def main():
    try:
        num = int(input(f"Enter an integer from 0 to {MAX_INPUT}: "))
    except (ValueError, EOFError):
        print("Please enter a whole number.")
        return 1

    if not 0 <= num <= MAX_INPUT:
        print(f"Please enter a number from 0 to {MAX_INPUT}.")
        return 1

    print("\n--- Countdown ---")
    countdown(num)
    print("\n--- Factorial ---")
    print(f"The factorial of {num} is {factorial(num)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
