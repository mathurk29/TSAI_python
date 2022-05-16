# Session 3 assignment of EPAi3.0
Numeric Types - I


* Integer Data Types
* Integer Operations
* Integer Constructors and Bases
* Rational Numbers
* Floats Internal Representation
* Floats Equality Testing
* Floats Coercing to Integer
* Floats Rounding

In Session 3 we discussed about the various Numeric Types available in Python. It is worth re-emphasizing that everything in Python is an object. Hence the basic data types explained here are implemented as Classes. Before going into details, let's first understand the term Base.

<br>
<br>

## Base:

The number of unique combination of digits available to represent numbers is called Base. For ex:
Binary base has two digits: [0. 1]. Decimal base has ten digits: from [0,1,2,3,4,5,6,7,8,9]. Hexadecimal base has 16 digits: {0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F].

<br>

Let's jump to basic data types supported by Python:

<br>

> bin() function

This returns the binary form of the integer. The binary form is indicated by prefixing '0b' to the encoding.

> hex() function:

This returns the hexadecimal form of the integer. The hexadecima form is indicated by prefixing '0x' to the encoding.
### __Integer__: 
An integer is a whole number with no decimal places.The clss  for the integer data type is int.

>type(10) \
> <class 'int'>

<br>
Note: If x is a number, return x.__int__().  

<br>
<br>
<br>

### __Float__: 
The float() method is used to return a floating point number from a number or a string

1. The left most digit stores the sign of the number.
2. The next eight digit stores the sign of the exponent on the base 10 and the binary representation of the value of the exponent.
4. The mantissa stores the binary 0b representation of the integer part of number.

![](https://www.puntoflotante.net/IEEE-754-ENGLISH.jpg)


<br>
<br>
<br>
<br>

## Various functions used in session3.py:

<br>

## from_base10()
This function converts a decimal in base 10 to it's representation in the suggested base. The mathematical equation used is:

The algorithm to create the encoding is:

if number is n and base is m:

    result = []
    while n > 0:
         m = n % b #DivFloor operator
         n = n // b #Modulus operator
         result.insert(0,n)

The above algorithm is derived from:

> Numerator = Denominator * DivFloor + __Modulus__


    For each iteration of the loop, the value of the _modulus_ is prefixed to the encoding.__

 
<br>
<br>
<br>

## encoded_from_base10()
This function returns a string encoding in the "base" for the "number" using the "digit_map"

This function supports conversion of decimal numbers to bases between 2 and 36 (including). It requires following params:

* The decmial number to be encoded
* The base to encode the number to. 
* A list of unique digits/letters which can be used to represent all numbers in that base. 

ValueError are raised if we see following errors:

Base is out-of-range.
digit_map is smaller than the base.
digit_map is not  long enough to encode digits


## encode()
A digit_map is a list of unique characters that are used to represent the number. 
This function converts the decimal digits to their corresponding representation in the suggested base using the digit_map.



## float_equality_testing()
This function emulates the isclose() method from the MATH module. It accepts two float numbers and compares them against two params:

__relative tolerance__: maximum difference for being considered "close", relative to the magnitude of the input v

__absolute tolerance__: maximum difference for being considered "close", regardless of the magnitude of the input values

    For this function we are going to assume:
    - rel_tol = 1e-12
    - abs_tol = 1e-05

For two numbers a and b, if at least one of the following condition happens to be true:

> abs(a- b) < abs_tol \

> (a-b)/max(a,b)  < rel_tol

then the numbers are considered to be close.


## manual_truncation_function()
This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point
The math.trunc() function has same behavior to that of int() function. Since int() function could not be used directly, as per the suggestion, we are using the constructor of float.__int__()

From the docs:

>help(float.__int__) \
>Help on wrapper_descriptor: \

> __int__(self, /)\
> return    int(self))


<br>

## manual_rounding_function():
This function emulates python's inbuild ROUND function, which rounds a number to the __nearest intger__. This is same rounding that we learnt in school.

If the decimal part is greater than 0.5 than the one is added to the integer part. The sign is kept as it is.

## rounding_away_from_zero()
This function rounds to the next integer away from zero on the number line.

Thanks!