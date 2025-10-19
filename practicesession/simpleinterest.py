def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.

    Parameters:
    principal (float): The principal amount.
    rate (float): The annual interest rate (in percentage).
    time (float): The time the money is invested for (in years).

    Returns:
    float: The simple interest calculated.
    """
    interest = (principal * rate * time) / 100
    return interest
# Example usage
if __name__ == "__main__":
    p = 1000  # Principal amount
    r = 5     # Annual interest rate in percentage
    t = 3     # Time in years

    si = calculate_simple_interest(p, r, t)
    print(f"The simple interest for a principal of {p}, rate of {r}%, over {t} years is: {si}")
    