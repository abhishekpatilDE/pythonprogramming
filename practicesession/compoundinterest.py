#!/usr/bin/env python3
"""Compound interest calculator

Defines a `compound_interest` function and prints an example when run as a
script. The original file included Markdown fences which prevented the code
from running; this file removes them so Python can execute the code.
"""


def compound_interest(principal, rate, times_compounded, years):
    """
    Calculate the compound interest.

    :param principal: Initial amount of money
    :param rate: Annual interest rate (decimal)
    :param times_compounded: Number of times interest is compounded per year
    :param years: Number of years the money is invested
    :return: Total amount after interest
    """
    amount = principal * (1 + rate / times_compounded) ** (times_compounded * years)
    return amount


# Example usage
if __name__ == "__main__":
    p = 1000  # Principal amount
    r = 0.05  # Annual interest rate (5%)
    n = 4     # Compounded quarterly
    t = 10    # Time in years

    total_amount = compound_interest(p, r, n, t)
    print(f"The total amount after {t} years is: {total_amount:.2f}")
