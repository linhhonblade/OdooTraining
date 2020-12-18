# Decorators
We will introduce decorators by repeating some **important aspects of functions**
## Important aspects of functions
- We can assign multiple names to the same function:

```python
def succ(x):
    return x + 1
successor = succ
successor(10)
```
Ouput: 11

- We can delete either "succ" or "successor" without deleting the function itself.

```python
del succ
successor(10)
```
Output: 11

- We can have or define functions inside of a function:

```python
def f():

    def g():
        print("Hi, it's me 'g'")
        print("Thanks for calling me")

    print("This is the function 'f'")
    print("I am calling 'g' now:")
    g()

f()
```
Output:
```
This is the function 'f'
I am calling 'g' now:
Hi, it's me 'g'
Thanks for calling me
```
Using return statements in the function:
```python
def temperature(t):
    def celsius2fahrenheit(x):
        return 9 * x / 5 + 32

    result = "It's " + str(celsius2fahrenheit(t)) + " degrees!"
    return result

print(temperature(20))
```
Factorial example:
```python
def factorial(n):
    """ calculates the factorial of n,
        n should be an integer and n <= 0 """
    def inner_factorial(n):
        if n == 0:
            return 1
        else:
            return n * inner_factorial(n-1)
    if type(n) == int and n >=0:
        return inner_factorial(n)
    else:
        raise TypeError("n should be a positve int or 0")
```
- Due to the fact that every parameter of a function is a reference to an object and functions are objects as well, we can pass functions - or better "references to functions" - as parameters to a function.
```python


def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")

def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    func()
    print("func's real name is " + func.__name__)

f(g)
```
Another example:
```python


import math

def foo(func):
    print("The function " + func.__name__ + " was passed to foo")
    res = 0
    for x in [1, 2, 2.5]:
        res += func(x)
    return res

print(foo(math.sin))
print(foo(math.cos))
```
- The output of a function is also a reference to an object. Therefore functions can return references to function objects.
This function returns (or generates) functions which can be used to create people in different languages:
```python
def greeting_func_gen(lang):
    def customized_greeting(name):
        if lang == "de":   # German
            phrase = "Guten Morgen "
        elif lang == "fr": # French
            phrase = "Bonjour "
        elif lang == "it": # Italian
            phrase = "Buongiorno "
        elif lang == "tr": # Turkish
            phrase = "Günaydın "
        elif lang == "gr": # Greek
            phrase = "Καλημερα "
        else:
            phrase = "Hi "
        return phrase + name + "!"
    return customized_greeting


say_hi = greeting_func_gen("tr")
print(say_hi("Gülay"))    # this Turkish name means "rose moon" by the way
```
Polynomial example:
```python


def polynomial_creator(a, b, c):
    def polynomial(x):
        return a * x**2 + b * x + c
    return polynomial

p1 = polynomial_creator(2, 3, -1)
p2 = polynomial_creator(-1, 2, 1)

for x in range(-2, 2, 1):
    print(x, p1(x), p2(x))
```
More general polynormial example:
```python
def polynomial_creator(*coefficients):
    """ coefficients are in the form a_n, ... a_1, a_0
    """
    def polynomial(x):
        res = 0
        for index, coeff in enumerate(coefficients[::-1]):
            res += coeff * x** index
        return res
    return polynomial

p1 = polynomial_creator(4)
p2 = polynomial_creator(2, 4)
p3 = polynomial_creator(1, 8, -1, 3, 2)
p4  = polynomial_creator(-1, 2, 1)


for x in range(-2, 2, 1):
    print(x, p1(x), p2(x), p3(x), p4(x))
```
Polynomial creator decorator avoiding exponentiation:
```python
def polynomial_creator(*coeffs):
    """ coefficients are in the form a_n, a_n_1, ... a_1, a_0
    """
    def polynomial(x):
        res = coeffs[0]
        for i in range(1, len(coeffs)):
            res = res * x + coeffs[i]
        return res

    return polynomial

p1 = polynomial_creator(4)
p2 = polynomial_creator(2, 4)
p3 = polynomial_creator(1, 8, -1, 3, 2)
p4 = polynomial_creator(-1, 2, 1)


for x in range(-2, 2, 1):
    print(x, p1(x), p2(x), p3(x), p4(x))
```
## A Simple Decorator
```python
def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

def foo(x):
    print("Hi, foo has been called with " + str(x))

print("We call foo before decoration:")
foo("Hi")

print("We now decorate foo with f:")
foo = our_decorator(foo)

print("We call foo after decoration:")
foo(42)
```
Output:
```
We call foo before decoration:
Hi, foo has been called with Hi
We now decorate foo with f:
We call foo after decoration:
Before calling foo
Hi, foo has been called with 42
After calling foo
```
After the decoration "foo = our_decorator(foo)", foo is a reference to the 'function_wrapper'. 'foo' will be called inside of 'function_wrapper', but before and after the call some additional code will be executed, i.e. in our case two print functions.

## This is the true decorator now
```python
def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

@our_decorator
def foo(x):
    print("Hi, foo has been called with " + str(x))

foo("Hi")
```
Output:
```
Before calling foo
Hi, foo has been called with Hi
After calling foo
```
- We can decorate every other function which takes one parameter with our decorator 'our_decorator
```python
def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        res = func(x)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper

@our_decorator
def succ(n):
    return n + 1

succ(10)
```
Output:
```
Before calling succ
11
After calling succ
```
- It is also possible to decorate third party functions, e.g. functions we import from a module. We can't use the Python syntax with the "at" sign in this case:
```python
from math import sin, cos

def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        res = func(x)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper

sin = our_decorator(sin)
cos = our_decorator(cos)

for f in [sin, cos]:
    f(3.1415)
```
- A generalized version of the function_wrapper, which accepts functions with arbitrary parameters:
```python
from random import random, randint, choice

def our_decorator(func):
    def function_wrapper(*args, **kwargs):
        print("Before calling " + func.__name__)
        res = func(*args, **kwargs)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper

random = our_decorator(random)
randint = our_decorator(randint)
choice = our_decorator(choice)

random()
randint(3, 8)
choice([4, 5, 6])
```

