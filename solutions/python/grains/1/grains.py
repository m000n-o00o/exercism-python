def square(number):
    '''
    Calculates the number of grains for a given square (without using a loop)
    It takes a specific square number (ranging from 1 to 64) and computes its value.
    '''
    if not (1 <= number <= 64):
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)
  


def total():
    """
    Calculates the total sum of grains across all 64 squares on the chessboard.
    """
    return (2 ** 64) - 1