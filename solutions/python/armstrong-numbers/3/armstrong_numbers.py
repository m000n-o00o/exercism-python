"""Module providing a function to check Armstrong numbers"""

def is_armstrong_number(number):
    """Check whether a number is an Armstrong number"""
    digits = str(number)        # text version, so we can loop over each digit
    digit_count = len(digits)             # number of digits (an int, used as the exponent)
    total = 0                   # starts at zero, before the loop
    for digit_char in digits:
        total += int(digit_char) ** digit_count   # convert the digit char to int, raise to the power digit_count
    return total == number      # True if the sum equals the original number