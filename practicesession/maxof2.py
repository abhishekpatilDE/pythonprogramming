#Find maximum of two numbers 

#!/usr/bin/env python3
"""Find maximum of two numbers

Simple script demonstrating a max function with a small driver.
"""

def maximum(a, b):
    """Return the larger of a and b."""
    return a if a > b else b


if __name__ == "__main__":
    # Driver code
    a = 10
    b = 20
    print("Maximum of", a, "and", b, "is", maximum(a, b))
