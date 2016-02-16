# Date and time
""""""""""""""""""""""""""""""""""""""""""
from datetime import datetime

now = datetime.now()
print now
print now.year
print now.month
print now.day
print '%s/%s/%s' % (now.month, now.day, now.year)
print '%s:%s:%s' % (now.hour, now.minute, now.second)
print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)

# Raw input
""""""""""""""""""""""""""""""""""""""""""
"""
Pig Latin is a language game, where you move the first letter of the word to the end and add "ay." So "Python" becomes "ythonpay."
"""

original = raw_input("Pig Latin").lower()
changed = original[1:] + original [0] + "ay"
print changed

changed.isalpha() # Check if the variable contains only alphabetical characters

# Type
""""""""""""""""""""""""""""""""""""""""""
print type(4)
print type(6.4)
print type("spam")

# Lists
""""""""""""""""""""""""""""""""""""""""""
"""
Lists are a datatype you can use to store a collection of different pieces of information as a sequence under a single variable name.
(Datatypes you've already learned about include strings, numbers, and booleans.)
"""

n = [1, 3, 5, 4]
n.pop(1)
# Returns 3 and delete it from the list
print n
# prints [1, 5, 4]
n.remove(1)
# Removes 1 from the list,
# NOT the item at index 1
print n
# prints [5, 4]
del(n[1])
# Doesn't return anything, delete the value at index 1
print n
# prints [5]


n = [3, 5, 7]

def print_list(x):
    for i in range(0, len(x)):
        print x[i]

print_list(n)


animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck") # 2
animals.insert(duck_index, "cobra") # Insert at that index
animals.remove("badger")
print animals


start_list = [5, 3, 1, 2, 4]
square_list = []
for number in start_list:
    square_list.append(number ** 2)
square_list.sort()
print square_list

""" List comprehension """
even_squares = [x**2 for x in range (1,12) if x%2 == 0]
print even_squares

cubes_by_four = [x**3 for x in range (1,11) if x**3%4 == 0]
print cubes_by_four
# Prints [8, 64, 216, 512, 1000]

# list comprehensions are better and faster than constructing a list in a loop with calls to append().
# When constructing a string, it is therefore better to construct a list first (which is mutable), then to create the string (which is immutable)

# create a concatenated string from 0 to 19 (e.g. "012..1819")
nums = [str(n) for n in range(20)]
print "".join(nums)

"""
One final thing to mention about strings is that using join() is not always best.
In the instances where you are creating a new string from a pre-determined number of strings, using the addition operator is actually faster,
but in cases like above or in cases where you are adding to an existing string, using join() should be your preferred method.
"""
foo = 'foo'
bar = 'bar'
foobar = foo + bar  # This is good
foo += 'ooo'  # This is bad, instead you should do:
foo = ''.join([foo, 'ooo'])

foo = 'foo'
bar = 'bar'
foobar = '%s%s' % (foo, bar) # It is OK
foobar = '{0}{1}'.format(foo, bar) # It is better
foobar = '{foo}{bar}'.format(foo=foo, bar=bar) # It is best

"""
Create a length-N list of lists
"""
four_nones = [None] * 4 # bad
"""
Because lists are mutable, the * operator (as above) will create a list of N references to the same list, which is not likely what you want.
Instead, use a list comprehension:
"""
four_lists = [[] for __ in xrange(4)] # good

""" Slicing """
to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens

to_21 = range(1,22)
odds = to_21[::2]
middle_third = to_21[7:14]

""" map() """
# Apply function to every item of iterable and return a list of the results.
a = [3, 4, 5]
a = [i + 3 for i in a]
# Or:
a = map(lambda i: i + 3, a)


# Dictionnaries
""""""""""""""""""""""""""""""""""""""""""
"""
A dictionary is similar to a list, but you access values by looking up a key instead of an index.
A key can be any string or number. Dictionaries are enclosed in curly braces, like so:
d = {'key1' : 1, 'key2' : 2}
"""
d = {}
d["chicken"] = 10.99
print d

zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}

del zoo_animals['Unicorn']
del zoo_animals['Bengal Tiger']
del zoo_animals['Sloth']
zoo_animals["Rockhopper Penguin"] = 'Other Exhibit'

my_dict = {
    "book": "Lord of the rings",
    "pages": 415,
    "suitedForKids": True
}

print my_dict.items()
print my_dict.keys()
print my_dict.values()

# List and dict
""""""""""""""""""""""""""""""""""""""""""
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort()

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold']+=50

#########################################
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]

#########################################
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
    total = float(sum(numbers))
    return total / len(numbers)

def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return homework * 0.1 + quizzes * 0.3 + \
    tests * 0.6

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return average(results)


print get_letter_grade(get_average(lloyd))
class_average = get_class_average([lloyd, alice, tyler])
class_letter_grade = get_letter_grade(class_average)
print class_average
print class_letter_grade

# Sets or lists?
""""""""""""""""""""""""""""""""""""""""""
# Take the following code for example:

s = set(['s', 'p', 'a', 'm'])
l = ['s', 'p', 'a', 'm']

def lookup_set(s):
    return 's' in s

def lookup_list(l):
    return 's' in l

"""
Even though both functions look identical, because lookup_set is utilizing the fact that sets in Python are hashtables, the lookup performance between the two is very different.
To determine whether an item is in a list, Python will have to go through each item until it finds a matching item.
This is time consuming, especially for long lists. In a set, on the other hand, the hash of the item will tell Python where in the set to look for a matching item.
As a result, the search can be done quickly, even if the set is large. Searching in dictionaries works the same way. For more information see this StackOverflow page.
For detailed information on the amount of time various common operations take on each of these data structures, see this page.

Because of these differences in performance, it is often a good idea to use sets or dictionaries instead of lists in cases where:
 - The collection will contain a large number of items
 - You will be repeatedly searching for items in the collection
 - You do not have duplicate items.
"""

# Range function
""""""""""""""""""""""""""""""""""""""""""
"""
The Python range() function is just a shortcut for generating a list, so you can use ranges in all the same places you can use lists.
The range() function has three different versions:
range(stop)
range(start, stop)
range(start, stop, step)
In all cases, the range() function returns a list of numbers from start up to (but not including) stop. Each item increases by step.
"""
range(6) # => [0,1,2,3,4,5]
range(1,6) # => [1,2,3,4,5]
range(1,6,3) # => [1,4]

"""
Iterating through list:
Now that we've learned about range, we have two ways of iterating through a list.

Method 1 - for item in list:
"""
for item in list:
    print item
"""
Method 2 - iterate through indexes:
"""
for i in range(len(list)):
    print list[i]
"""
Method 1 is useful to loop through the list, but it's not possible to modify the list this way.
Method 2 uses indexes to loop through the list, making it possible to also modify the list if needed.
"""



# While
""""""""""""""""""""""""""""""""""""""""""
"""
Something completely different about Python is the while/else construction. while/else is similar to if/else, but there is a difference:
the else block will execute anytime the loop condition is evaluated to False.
This means that it will execute if the loop is never entered or if the loop exits normally.
If the loop exits as the result of a break, the else will not be executed.

Similarly with for loops. Else is not executed if the loop is broken
"""

# Enumerate
""""""""""""""""""""""""""""""""""""""""""
""" enumerate works by supplying a corresponding index to each element in the list that you pass it. """
choices = ['pizza', 'pasta', 'salad', 'nachos']
print 'Your choices are:'
for index, item in enumerate(choices):
    print index+1, item

# Zip
""""""""""""""""""""""""""""""""""""""""""
"""
zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list.
zip can handle three or more lists as well!
"""
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    if a > b:
        print a
    else:
        print b

keys = ['a', 'b', 'c']
values = [1, 2, 3]
hash = {k:v for k, v in zip(keys, values)} # Creates a dictionnary
#hash
#{'a': 1, 'c': 3, 'b': 2}

# Reverse
""""""""""""""""""""""""""""""""""""""""""
"""This is extended slice syntax. It works by doing [begin:end:step] - by leaving begin and end off and specifying a step of -1, it reverses a string."""
'hello world'[::-1]
# 'dlrow olleh'
""" Without using this """
def reverse(text):
    result = ""
    while len(text) != 0:
        result += (text[len(text)-1:len(text)])
        text = text[:len(text)-1]
    return result

#Or to do better, let's use a list first as it is less time consuming like we saw before
def reverse2(text):
    result = []
    while len(text) != 0:
        result.append(text[len(text)-1:len(text)])
        text = text[:len(text)-1]
    return ''.join(result)

# Anonymous functions
""""""""""""""""""""""""""""""""""""""""""
lambda x: x % 3 == 0
#Is the same as
def by_three(x):
    return x % 3 == 0

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)
# Prints [0, 3, 6, 9, 12, 15]

# Build a list of the squares of the numbers between 1 and 10 with a list comprehension
squares = [x**2 for x in range(1,11)]
# print out only the squares between 30 and 70
print filter(lambda x: x >= 30 and x <= 70, squares)

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x!= 'X', garbled)
print message

# Binary representation
""""""""""""""""""""""""""""""""""""""""""
# Prefixing a variable value with 0b will give the binary value
nine = 0b1001
print nine
# bin() function converts an interger to binary
bin(9)
# When given a string containing a number and the base that number is in, the function will return the value of that number converted to base ten.
print int("11001001",2)

# Bitwise operators
""""""""""""""""""""""""""""""""""""""""""
# Left Bit Shift (<<)  equivalent to multiplying by 2 for every time you shift
0b000001 << 2 == 0b000100 (1 << 2 = 4)
0b000101 << 3 == 0b101000 (5 << 3 = 40)

# Right Bit Shift (>>) equivalent to a floor division by 2 for every time you shift
0b0010100 >> 3 == 0b000010 (20 >> 3 = 2)
0b0000010 >> 2 == 0b000000 (2 >> 2 = 0)

shift_right = 0b1100
shift_left = 0b1

shift_right = shift_right >> 2
shift_left = shift_left << 2

print bin(shift_right) # 0b11, 3
print bin(shift_left) # 0b100, 4

# Octal
0o177
# Hexa
0x9ff

# AND (&) operator
"""
The bitwise AND (&) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on
if the corresponding bits of both numbers are 1. For example:
a:   00101010   42
b:   00001111   15
===================
a & b:   00001010   10
"""
print bin(0b1110 & 0b101) # 0b100, 4

# OR (|) operator
# The bitwise OR (|) operator compares two numbers on a bit level and returns a number where the bits of that number are
# turned on if either of the corresponding bits of either number are 1.
print bin(0b1110 | 0b101) # 0b1111

# XOR (^) operator
# The XOR (^) or exclusive or operator compares two numbers on a bit level and returns a number where the bits of that number are turned on
# if either of the corresponding bits of the two numbers are 1, but not both.
print bin(0b1110 ^ 0b101) # 0b1011

# NOT (~) operator
# Add one to the number and makes it negative
print ~1 # -2
print ~2 # -3
print ~3 # -4

# mask
# with $, check if a specific bit is on
num  = 0b1100
mask = 0b0100
desired = num & mask
if desired > 0:
    print "Bit was on"

# with |, turn a specific bit on
a = 0b110 # 6
mask = 0b1 # 1
desired =  a | mask # 0b111, or 7

# with ^, filp all the bits
a = 0b11101110
mask = 0b11111111
desired = a ^ mask
print bin(desired) # 0b10001

# Classes
""""""""""""""""""""""""""""""""""""""""""
"""
A basic class consists only of the class keyword, the name of the class, and the class from which the new class inherits in parentheses.
Passing object to a new class gives it the powers and abilities of a Python object.
By convention, user-defined Python class names start with a capital letter.
"""

class Animal(object):
    pass # pass doesn't do anything, but it's useful as a placeholder in areas of your code where Python expects an expression.

"""
Class Scope
Another important aspect of Python classes is scope. The scope of a variable is the context in which it's visible to the program.
It may surprise you to learn that not all variables are accessible to all parts of a Python program at all times.
When dealing with classes, you can have variables that are available everywhere (global variables),
variables that are only available to members of a certain class (member variables),
and variables that are only available to particular instances of a class (instance variables).
"""
class Animal(object):
    """Makes cute animals."""
    is_alive = True # Member variable
    def __init__(self, name, age):
        self.name = name
        self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print zebra.name, zebra.age, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_alive
print panda.name, panda.age, panda.is_alive

# Inheritance
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours) # Using super to directly access the methods and attributes of the super class

milton = PartTimeEmployee("Milton")
print milton.full_time_wage(1)

# Other inheritance example
class Triangle(object):
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def check_angles(self):
        return self.angle1 + self.angle2 + self.angle3 == 180

my_triangle = Triangle (90, 30, 60)
print my_triangle.number_of_sides
print my_triangle.check_angles()

class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle

# Car
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg

    def display_car(self):
        return "This is a %s %s with %s MPG." % (self.color, self.model, self.mpg)

my_car = Car("DeLorean", "silver", 88)
print my_car.condition
print my_car.display_car()

# REPR
"""
The method __repr__ tells Python how to represent that object when we print it out.
"""
class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point = Point3D(1, 2, 3)
print my_point


# File input/output I/O
""""""""""""""""""""""""""""""""""""""""""
""" Open output.txt in 'r+' mode: read and write
	r: read
	w: write
"""
my_file = open("output.txt", "r+")

my_list = [i**2 for i in range(1,11)] # List comprehension
my_file = open("output.txt", "r+") # Open the file in read and write mode
for item in my_list:
    my_file.write(str(item) + "\n") # Write each element of the list to the file
my_file.close() # Close the file

my_file = open("output.txt", "r")
print my_file.read()
print myfile.readline() # Gets just one line at a time
my_file.close()

""" A file NEEDS to be closed after being read or written into
	One way of not having to invoque the close() method is to use with / as:
"""
with open("text.txt", "w") as textfile:
	textfile.write("Success!")

# The with statement is better because it will ensure you always close the file, even if an exception is raised inside the with block.

# Check of the file is actually closed
if not textfile.closed:
    textfile.close()

print textfile.closed

# Import modules, best practices
"""
http://docs.python-guide.org/en/latest/writing/structure/
Any directory with an __init__.py file is considered a Python package.
Leaving an __init__.py file empty is considered normal and even a good practice, if the package’s modules and sub-packages do not need to share any code.

Very bad
[...]
from modu import *
[...]
x = sqrt(4)  # Is sqrt part of modu? A builtin? Defined above?

Better
from modu import sqrt
[...]
x = sqrt(4)  # sqrt may be part of modu, if not redefined in between

Best
import modu
[...]
x = modu.sqrt(4)  # sqrt is visibly part of modu's namespace


import very.deep.module as mod. This allows you to use mod in place of the verbose repetition of very.deep.module.
"""
