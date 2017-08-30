## Mathematical Operators

Using IPython to run the follow commands

- Addition

3 + 5 = 8

- Subtraction

10 - 5 = 5

- Multiplication

3 * 5 = 15

- division

30 / 6 = 5

- Exponent

2 ** 2 = 4

- Negation

-2 + -3 = -5

Integers and Floats

Int -> 35
Float -> 30.5

Order of Operations

(5 + 7) * 3 = 36
  12    * 3

5 + 7 * 3 = 26
5 +  21

* PEMDAS: Parentheses Exponent Multiplication Division Addition Subtraction


https://www.python.org/dev/peps/pep-0008/

## Using variables

```python
    a = 1
    b = "abc"
    c = 23.3
    d = []
    e = {}
    f = ()
```

Import Modules

```python
    import math

    num_a = 4.8
    math.ceil(num_a)
```
Libraries

https://docs.python.org/2.7/library/

## Strings

### Strings are a sequence of characters that can store letters, numbers, or a combination — anything!

```python
>>> 'Hello World'

>>> "SPAM99"

>>> first_name = 'Learn'
>>> last_name = 'Python'
>>> full_name = first_name + last_name

>>> full_name
```

### Concatenating a Space

```python
>>> first_name = 'Learn'
>>> last_name = 'Python'
>>> full_name = first_name + last_name

>>> full_name
```

### Moving our code to a script file

* Create a script.py

```python
    first_name = 'Monty'
    last_name = 'Python'
    full_name = first_name + ' ' + last_name 

    print(full_name) #py2 and py3, in py2 print doesn't need ()
```
```shell
    $ python script.py
```

### Concatenating String and Ints

```python
    # Describe the sketch comedy group
    name = 'Monty Python'
    description = 'sketch comedy group'
    year = 1969
    # Introduce them
    Year is an int, not a string
    sentence = name + ' is a ' + description + ' formed in ' + year
```

### Turning an Int into a String

```python
    # Describe the sketch comedy group
    name = 'Monty Python'
    description = 'sketch comedy group' year = 1969
    #  Introduce them
    Instead, convert the int to a string when we concatenate with str()
    sentence = name + ' is a ' + description + ' formed in ' + str(year) 
    print(sentence)
```

### print() Casts to String Automatically

```python
    # Describe the sketch comedy group
    name = 'Monty Python'
    description = 'sketch comedy group' year = 1969
    # Introduce them
    print() does string conversions for us
    print(name, 'is a', description, 'formed in', year)
```

### Dealing With Quotes in Strings

-> Wrong
##### Describe Monty Python's work

```python
    famous_sketch = 'Hell's Grannies'
```

-> Correct

##### Describe Monty Python's work

```python
    famous_sketch1 = "Hell's Grannies" 
    print(famous_sketch1)
```

### Special characters -- \n \t

##### Describe Monty Python's work

```python
    famous_sketch1 = "\n\tHell's Grannies"
    famous_sketch2 = '\n\tThe Dead Parrot'
    print('Famous Work:', famous_sketch1, famous_sketch2)
```


### String behind the Scenes

```python
    >>> word = 'hello world'
    >>> word[0]
    >>> word[11]
    >>> word[12]
```

### String Built-in Function -- len()

```python
    >>> word = 'hello world'
    >>> len(word)
```

### Joking with strings

```python
    >>> word = 'Hello 99ner'
    >>> end = word[2] + word[6]
    >>> print(end)
```

### Using slices to access parts of a string

```python
    >>> word = "Python"
    >>> word[2:5]
    >>> 'tho'
 ```

 ### Slice Formula and Shortcuts

 * slice formula: variable [start : end+1]

 ```python
    >>> word = "Good"
    >>> word[0:2]
    >>> word[:2]
    >>> Go

    >>> word[2:4]
    >>> word[2:]
    >>> od
 ```

### Incoporating String slices into our solution

```python
    >>> word1 = 'Good'
    >>> end1 = word1[2] + word1[3]
    >>> word1[2:4] 
    >>> print(end1)
```

### The index at the halfway point

#### Calculate the halfway index

* The len() function will let us calculate the halfway index of our word.

```python
    word1 = 'Good' 
    half1 = len(word1)/2
    word2 = 'Evening' 
    half2 = len(word2)/2
```

### The index at the halfway point

* // 2 division signs means integer division in Python.

```python
    word1 = 'Good'
    half1 = len(word1)//2
    word2 = 'Evening' 
    half2 = len(word2)//2
```


### Making our program more reusable

```python
    word1 = 'Good'
    half1 = len(word1)//2
    end1 = word1[2:] 
    word1[half1:] 
    word2 = 'Evening'
    half2 = len(word2)//2
```


## Conditional Rules of Engagement

```shell
    < less than
    <= less than equal to
    == equal to
    >= greater than equal to
    > greater than
    != not equal to
```

### Conditional -- if, then

```python

    # Battle Rules
    num_knights = 2
    if num_knights < 3:
        print('Retreat!')
        print('Raise the white flag!')
```

```python
    # Battle Rules
    num_knights = 4
    if num_knights < 3:
        print('Retreat!')
        print('Raise the white flag!')
```

### The program continues after the conditional

```python
    # Battle Rules
    num_knights = 4
    if num_knights < 3:
        print('Retreat!')
        print('Raise the white flag!') 
    print('Knights of the Round Table!') 
```

### Rules for whitespace in Python

```python
    if num_knights == 1: # Block start
    print('Do this') 
      print('And this')
    print('Always this')
```

### Conditional -- if False -> else

```python
    # Battle Rules
    num_knights = 4
    if num_knights < 3:
        print('Retreat!')
    else:
        print('Truce?')
```

### Conditionals -- How tocheck another condition?

* *elif*  Allows Checking Alternatives

```python
    # Battle Rules
    num_knights = 10
    day = 'Wednesday'
    if num_knights < 3: 
        print('Retreat!')
    elif num_knights >= 10: 
        print('Trojan Rabbit')
    elif day == 'Tuesday': 
        print('Taco Night')
    else: 
        print('Truce?')
```

### Combining conditionals with *and/or*


#### Putting *or* in our program
```python
    if num_knights < 3 or day == "Monday": 
        print('Retreat!')
```


#### Putting *and* in our program

```python
    if num_knights >= 10 and day == "Wednesday": 
        print('Trojan Rabbit!')
```


### Incorporating the days of the week

```python
    # Battle Rules
    num_knights = 10
    day = 'Wednesday'
    if num_knights < 3 or day == 'Monday': 
        print('Retreat!')
    elif num_knights >= 10 and day == 'Wednesday': 
        print('Trojan Rabbit!')
    else: 
        print('Truce?')
```



## User input -- With the input() function

```python
    # Ask the user to input the day of the week
    day = input('Enter the day of the week')
    print('You entered:', day)
```

### Receiving user input from console

```python
    num_knights = int(input('Enter the number of knights'))
    User enters #, but it comes in as text
    print('You entered:', num_knights) 
    if num_knights < 3 or day == 'Monday':
        print('Retreat!')
``` 

### Different input and conditionals changes output

* Different user input causes different program flow

```python
    # Battle Rules
    num_knights = int(input('How many knights?')) 
    day = input('What day is it?'))
    if num_knights < 3 or day == 'Monday': 
        print('Retreat!')
    elif num_knights >= 10 and day == 'Wednesday': 
        print('Trojan Rabbit!')
    else: 
        print('Truce?')
```

### Nested Conditionals

```python
    # Battle Rules
    num_knights = int(input('Enter number of knights') 
    day = input('Enter day of the week')
    enemy = input('Enter type of enemy')
    if enemy == 'killer bunny': 
        print('Holy Hand Grenade!')
    else:
    # Original Battle Rules
    if num_knights < 3 or day == 'Monday': 
        print('Retreat!')
    if num_knights >= 10 and day == 'Wednesday': 
        print('Trojan Rabbit!')
    else: print('Truce?')
```
