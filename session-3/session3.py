from fractions import Fraction

def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module

    '''
    if base < 2 or base > 36:
        raise ValueError("Invalid base: 2 <= base <= 36")
    if len(digit_map) != len(set(digit_map)):
        raise ValueError("Are you giving repeating values.")
    sign = -1 if number < 0 else 1
    number *= sign

    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)

    if sign == -1:
        encoding = "-" + encoding

    return encoding


def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not long enough to encode digits")

    encoding = "".join([digit_map[d] for d in digits])
    return encoding


def from_base10(n, b):
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        # m = n % b
        # n = n // b
        # which is the same as:
        n, m = divmod(n, b)
        # insert at right most place
        digits.insert(0, m)
    return digits


def float_equality_testing(a, b):
    '''
    This function emulates the ISCLOSE method from the MATH module, but you can't use this function
    We are going to assume:
    - rel_tol = 1e-12
    - abs_tol = 1e-05
    '''
    rel_tol = 1e-12
    abs_tol = 1e-05
    diff = abs(a - b)
    return True if diff <= abs_tol or diff / max(abs(a), abs(b)) <= rel_tol else False


def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
    '''
    assert f_num == f_num.__float__() , "The argument passed is not float"
    return f_num.__int__()


def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    '''

    int_part_with_sign = manual_truncation_function(f_num)
    dec_part = abs(f_num - int_part_with_sign)

    sign = -1 if int_part_with_sign < 0 else 1
    int_part = int_part_with_sign * sign

    if dec_part > 0.5:
        int_part += 1
    return sign*int_part


def rounding_away_from_zero(f_num):
    '''
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't. 
    Hint: use FRACTIONS and extract numerator. 
    '''
    if Fraction(f_num).denominator == 1:
        return Fraction(f_num).numerator
    elif Fraction(f_num).numerator == 0:
        return 0
    div_floor = Fraction(f_num).numerator  // Fraction(f_num).denominator

    if Fraction(f_num).numerator > 0:
        return div_floor + 1
    else:
        return div_floor
