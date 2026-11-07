# Countdown and Factorial Calculator

A Python command-line program that counts down from a whole number and then calculates its factorial.

## Run

Requires Python 3. No third-party packages are needed.

```sh
python3 "Countdown&Factorial_Calculator.py"
```

Enter an integer between 0 and 1000. For example, entering 5 prints a countdown from 5 to 1, followed by `Blastoff!` and a factorial of `120`. Entering 0 prints `Blastoff!` immediately and gives a factorial of `1`.

The countdown uses a loop, and the factorial uses Python's standard library. The input limit keeps the terminal output manageable. Invalid input prints a message and exits with status 1.
