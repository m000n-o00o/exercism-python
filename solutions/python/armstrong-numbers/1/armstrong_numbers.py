def is_armstrong_number(number):
    digits = str(number)        # text version, so we can loop over each digit
    y = len(digits)             # number of digits (an int, used as the exponent)
    total = 0                   # starts at zero, before the loop
    for ch in digits:
        total += int(ch) ** y   # convert the digit char to int, raise to the power y
    return total == number      # True if the sum equals the original number