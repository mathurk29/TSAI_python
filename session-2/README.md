# Session 2 assignment of EPAi3.0
Object Mutability and Interning
# Cyclic Reference

## The problem may initially looked puzzling but becomes digestable when one chews one bite at a time i.e. consider a simple case where collection has only one element. **Divide and Rule!** 

The following explanation is based on above apporach and the solution is *inaffected* with the length of the collection list. 

On invoking *critical_function()*, the *add_something()* function is called: 

`something = Something()`

    Let's say something is pointing to memeory location xyzabc1. Refer Fig1
    As per the __init__() function the following assignment will occur: 
    ref_count(xyzabc1) = 1
    
    *something.something_new* =  None.


![](https://i.ibb.co/c19kX7M/image.png)

`something.something_new = SomethingNew(i, something)`

    **Lets take RHS first.**

    An object for SomethingNew is created, let's say at abcxyz2:
    As per the __init__() function the following assignment will occur: :
    - self.i = 1,
    - self.something = xyzabc1

![](https://i.ibb.co/Lx5tYx8/image.png)
   
   
    **Now consider LHS:**

    The reference to above object is set to  *something.something_new*. Hence now:

    as per the __init__() function the following assignment will occur: :
    - something.something_new = abcxyz2
    - *something.something_new*.i = 1
    - *something.something_new*.something = xyzabc1

    - appending something to collection creates another reference to xyzabc1. thus
        ref_count(xyzabc1) = 2
    
    - scope of function is reached and something(reference to xyzabc1) is cleared.
        thus ref_count(xyzabc1) = 2

![](https://i.ibb.co/ZJq5D7b/image.png)

`collection.clear() `

    This deletes the elements inside the collection list which are nothing but references  to xyzabc1. So now only objects referenceing xyzabc1 is
    `something.something_new**.something`

    Here we can see the cyclic reference. Both objects are referenced by each other's data members and no othere varibales.

**Here is the representation of cyclic reference**  

![](https://i.ibb.co/Krx9Mjq/image.png)
---

## Solution: gc has started handling cyclic references very well. We After removig all the references to the objects of classes Something and Something_new in clear_memory(), we are left with dangling cyclic references in the forest. gc.collect() function will identifies those cyclic reference and deletes them from memory.** 

---

    Tadaaa!
![The dancing kid](https://i.ibb.co/FntqYCq/475c6a0422609b2017be41416e2075fc.gif)





--- 
# String Interning

The function compare_strings_old() was ineffective as it was using brute force to compare two large strings. Also parsing the entire string does not make sense, one should simply collect all the occuring alphabets in the string and then search the required character in the generated list.

Since the two variables had same value, rather than created two memeory locations with that value, we could force Python to assign that value to just one location and assign that to the two references `a` and `b`.

This can be done by Python Interning - where frequently used values are stored at preset memory locations by Python INterpreter. If any of those values are assingned to some variable, the variable is set as a reference to its *interned* memory location.

## Thus simply comparing the ids of a and b (using is operator) in compare_strings_new() confirmed that the value is equal as well!


sleep delays execution for n number of seconds. As advised it was removed.

# Sring comparison

## char_list was simply changed to set. The required char was then checked to bre present in this set with just all unique alphabets to quickly find its presence!