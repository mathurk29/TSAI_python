# epai3session5

# Session 5 - Functional Parameters

## Unpacking of Iterables

Anything which can be iterated can be unpacked. For ex: tuple, list, string etc.

```
(a,b,*c,d,e) = Pythonista

a = p
b = y
c = t,h,o,n,i,s,t
d = t
e = a
```


## Arguments & Parameters


```python
def my_func(a, b): 
    code 
```

a and b are called __parameters__ of *my_func* and are local to *my_func*.

```python
x = 10 
y = 20
my_func(x, y) 

```
x and y are called the **arguments** of my func  Also note that x and y are passed by reference 

--- 

## Postional Arguments / Default Arguments / Non-keyword arguments == Tuple(,)
- Arguments unpacked based on order 
- If default values are given for a parameter, all params to the right should be provided default values. They are called **default arguments**.
- Arguments are assigned to Parameters based on extended unpacking explained above
- while unpacking when `*args` is encountered, all the remaining unpacked variables are scopped into the `*args`.

- There can be no positional arguments after `*`. Thus it restricts the number of positional arguments availabe to the function.

    For ex:
    ```python
    f1 has just two positional arguments `a` and `b`. f2 has no positional arguments.

    def f1(a,b,*,c,d):
        code

    def f2(*,c,d):
        code
    ```



    <a href="https://ibb.co/p27xgCC"><img src="https://i.ibb.co/SNjP2qq/image.png" alt="image" border="0"></a>

<br> 

---

## Keyword Arguments / Named Arguments / Unordered -- {Dictionary}

- Arguments based on names.
- all arguments to the right of `*args` or `* `are keywored arguments
- We can make a keyword argument mandatory by explictly defining it in the declaration.
- **kwargs scoop all arguments which were not explicitly present in the function declaration!



    <a href="https://ibb.co/nMR4NPy"><img src="https://i.ibb.co/VY3bcwG/image.png" alt="image" border="0"></a>

    <a href="https://ibb.co/pRmcRFg"><img src="https://i.ibb.co/rcWYcrg/image.png" alt="image" border="0"></a>

    *BEWARE*: Default arguments are evaluated **just once** when function definition is executed and that value remains in memory unless value is set explicitly in function call.

<br>
<br>
<br>
<br>
<br>

---

# Lambda Expression

```
#defining the function
def function_name(parameter_list):
    expression

#calling the function
a = function_name()
```
can be written one-liner as:
```
a = lambda parameter_list: expression
```

<br>
---

# Docstrings & Annotations

*PEP 257:* 

    If the first line in the function body is a string (not an assignment, not a comment, just a string by itself), it will be interpreted as a docstring.

    docstring is stored in **\_\_doc__** attribute of the object.

    **help**(object) also shows the content of docstring.

*PEP 3107* 

    Annotation are <expressions> which are used to describe the parameters and return values of the object. They are generally used to specify types, however note they do not restrict 

    They are stored in the **\_\_annotation__** attribute of the object.

    **help**(object) also shows the content of annotations.


<br>
---

# session5.py

> time_it(fn, *args, repetitions= 1, **kwargs)

gives out the average run time per call.
    
    param:
        fn: function  - which needs to be timed.
        repetitions: number - number of times to call the function
        args: positional argumets to be passed to fn.
        kwargs: keyword arguments to be passed to fn.

    return: 
        average: float - average time taken by fn to run repetitions number of times.



> squared_power_list()

Returns list by raising number to power from start to end 
    -> number**start to number**end. Default start is 0 and end is 5

    param:
        1. number: int 
        2. start: int
        3. end: int

    returns: 
        list

> polygon_area()

Returns area of a regular polygon with number of sides between
3 to 6 bith inclusive. If additional positional/ keyword arguments are given, error is raised.

    param:
        length: int   - length of each side of polygon
        args   - captures additional positional arguments to raise error.
        sides: int - default = 3. Total no of sides of the polygon
        kwargs - captures keyword positional arguments to raise error.

    return:
        result: float - area of the polygon


> temp_converter()

Converts temprature from celsius 'c' to fahrenheit 'f' or fahrenheit to celsius

    param:  
        temp: int  - temperature to be converted
        args: to capture additional positional parameteres, if present, and used to raise error.
        temp_given_in: str - acceptable value - F or C - to tell the unit of temperature providied in temp
        kwargs: to capture additional keyword parameteres, if present, and used to raise error.
    
    return: 
         result: float - temperature value converted to the other unit.

> speed_converter()

Converts speed from kmph (provided by user as input) to different units dist can be km/m/ft/yrd time can be ms/s/min/hr/day
speed: int, *args, dist='km', time='min', **kwargs) -> float: