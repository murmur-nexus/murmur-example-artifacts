import sys
from sympy import isprime

def is_prime(expression):
    try:
        # Attempt to convert the expression to an integer
        number = int(expression)
        # Check if the number is prime
        return isprime(number)
    except ValueError:
        # Handle cases where the input cannot be converted to an integer
        print(f"Error: '{expression}' is not a valid integer.")
        return False
    except Exception as e:
        # Catch other unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        return False


if __name__ == "__main__":
    expression = " ".join(sys.argv[1:])
    print(is_prime(expression))