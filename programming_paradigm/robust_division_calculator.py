# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """Performs division with robust error handling for invalid inputs and division by zero."""
    try:
        # Convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Try performing the division
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        # Handles non-numeric input
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        # Handles division by zero
        return "Error: Cannot divide by zero."
