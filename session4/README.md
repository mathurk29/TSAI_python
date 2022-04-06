# Session 4 - Numeric Types II & Functional Arguments
## Floats: Coercing to Integers

There are several ways to optimise the data loss as per our requirements 

1. **Truncation**: simply return the integer portion and ignore everything after the decimal point. 
    `math.trunc() `

    `int() constructor.`
2. **Floor**: return the largest integer less than or equal to the number itself.

    `math.floor()`
3. **Ceiling**: return the smallest integer equal to or just greater than the number itself.

<br>
<br>
---

## Floats: Rounding

    The round() function is sd
    Python provides a built-in rounding function: round(x, n=ø).

    This will round the number x to the closest multiple of 10^(-n).

    In addition to truncate, floor, and ceiling, we can therefore also use rounding to coerce a float to an integer number 

    If n is not specified, then it defaults to zero and round(x) will therefore return an int 

        round(x)  -> int

        round(x, n)  -> same type
        
        round(x, e)  -> same type

    As per IEEE 754 standard, Python follows Banker's Rounding implementation for tie breaking. 

    **This algorithm suggests to round to the nearest value with even least significant digit**

    For ex: 
    round(1.25)  -> 1.2
    round(1.35)  -> 1.4
    round(15, -1)  -> 20
    round(25, -1)  -> 20



<br>
<br>


---


## Booleans

Python has a `bool class` which can have just two instances - `True` and `False`
This is a subclass of `int class`
`True` and `False` are singleton objects we can use both `==` or `is` for comparison 
>  `bool(None)` is evaluated to `False`

> 	`1 == 2 == False` means `1 == 2 AND 2 == False`

> `bool(0), bool(0.0), bool(Fraction(0,1)), bool(Decimal('0')), bool(0j) bool([]), bool(()), bool('') `  are all `False`

Every object has a True truth value, except: 

* None 
* False 
* O in any numeric type (e.g., O, 0.0, 0+0j, )
* empty sequences (e.g. list, tuple, string,) 
* empty mapping types (e.g. dictionary, set) 
* custom classes that implement a __bool__  or __len__ method that returns False or 0 on False Truth value


<br>
<br>
<br>


--- 
## Booleans: Precedence and Short-Circuiting

> X or Y - If X is **True**: will always return **True**
>
> X and  Y - If X is **False** : will always return **False**



<br>
<br>
<br>
<br>


# Dunder functions of session4.py

The Qualean class is inspired by Boolean+Quantum concepts. 
Either We can assign it the 3 possible real states or its . True, False, and Maybe (1, 0, -1) or it will randomly choose any  one state.

**Truthy Value**  -  False if state is 0 otherwise True.
The moment it is assigned a state, it immediately finds an imaginary number random.
## __and__

This returns True except when:
1. q2 is not defined
2. either q1 or q2 are False

## __or__

This returns True when:
1. q2 is not defined
2. Both q1 and q2 are False

## __repr__

Tells that the object is an instance fo Qualean class.

## __str__

Gives string representation of the number stored by the Qualean class.

## __add__

Checks for proper type (Qualean/Float) otherwise raises TyperError.
returns simple addition of the `number` member of the two qualean objects.

## __eq__
Checks for proper type (Qualean/Float) otherwise raises TyperError.
Compares `number` member of the two qualean objects.

## __float__

Simply convert the `number` member into its float form.

## __ge__

Checks for proper type (Qualean/Float) otherwise raises TyperError.
This compare the `number` member and tells whether the `number` member of the self is greater or equal than the `number` member object of the object passed in argument.

## __gt__

Checks for proper type (Qualean/Float) otherwise raises TyperError.
This compare the `number` member and tells whether the `number` member of the self is greater than the `number` member object of the object passed in argument.

## __invert__

It reverses the sign of the `number` member by multiplies it by -1.

## __le__

Checks for proper type (Qualean/Float) otherwise raises TyperError.
This compare the `number` member and tells whether the `number` member of the self is less or equal than the `number` member object of the object passed in argument.


## __lt__

Checks for proper type (Qualean/Float) otherwise raises TyperError.
This compare the `number` member and tells whether the `number` member of the self is less than the `number` member object of the object passed in argument.



## __mul__

Checks for proper type (Qualean/Float) otherwise raises TyperError.
Returns the mathematical multiplication of the  `number` member of the two Qualean objects.

## __sqrt__

Returns the square root of the `number` member. 
If the `number` membe is negative, it calls the invertsign to convert the `number` member into positve and then suffixes 'i' for representing imaginary part.

## __bool__

Simply returns the Truthy Value of the `number` member of the Qualean class.

## __init__

Accepts input only in one of the possible states - True/False/Maybe or  raises ValueError.

If no state is provided, randomly chooses an inital state.

Once the state is assigned, it immediately select a random number between [-1 and 1], multiply it with the state value and store that number internally. There are various dunder methods to operate on this `number`.

--- 
Thank You!