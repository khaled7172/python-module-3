*This project has been created as part of the 42 curriculum by khhammou*

## Description

In python to use command-line arguments import sys
sys.argv built-in list that stores command-line arguments passed to a script when it is executed
first element is always the script name
script_name = sys.argv[0] # name of the script 
sys.argv[1] actual first argument by user
etc..
All items stored as strings
seperated by spaces
to pass an argument that contains spaces enclose it in ""
len(sys.argv) to find total nb of items
to get a list of only user-provided arguments use
user_args = sys.argv[1:]
range(start, stop) goes from start to stop - 1
use {sum:.2f}
.2f is for 2 points after decimal
cd .. && mkdir -p ex3 && cd ex3
get out, create directory if it doesn't exit and enter it

Dictionary(map)
it maps keys to values
in ex3 it is mapping names(keys) to sets(values)
.items() gives you key-value pairs from the dictionary
To print all distinct items across sets
use the union or the | operator
example
unique = set1 | set2 | set3
unique = set1.union(set2, set3)
|(union) every distinct element from all sets
&(intersection) only items present in all three sets
-(Difference) items in first set not found in others
^(Symmetric difference) items in exactly one set not repeated in other one
Symmetric difference of two sets A and B
is the set of elements that are in A or B but not in Both
Reading command-line arguments in dictionary format:
you loop over the arguments skipping the program name
example input, program_name sword:1
you split on the colon so key has sword and value has 1
then you set the value inside the dictionary
dict[key] = int(value)
To access all values in the dict use dict.values()
you can sum the values this way
for keys, you cant use sum, use len(dict.keys())
To find min and max elements in a dictionary
you could use max(dict.values())
but if you want it with the key you have to use the .get() method
why we check if key is None?
because if key is none, inventory.get(None)
will raise an error in python
you cant compare an int with None
sample lookup is done without accessing the keys
you are looking for a key, return True or False depending on if the key exists inside the dict or not
{'key' in dict}
enumerate is good if you want an index with the values or for a specific case you want to do ata specific index
to print commmas instead of doing it after words, do it before you print a word if the word exists
if checks first
elif only runs if previous if was False and value checked is true
else only runs if neither if or elif was True
else is not a global "catch all" it only applies to the if above it which may create problems with multiple if statements, so use elif
Generation:
yield is a regular function that does its work and returns once
A generator function pauses at yield, give you a values
then remembers where it left off
Next time you ask for a value via next() or for loop it continues from there
meaning we dont store 1000 events in memory, you generate them on demand
example:
def count_up_to(n):
    for i in range(n):
        yield i
gen = count_up_to(3)
you can get the next values one by one:
print(next(gen)) # 0 
print(next(gen)) # 1
and so on.
After the last value, next() will raise StopIteration
iter() Turns any iterable (like a list) into an iterator
example:
lst = [10, 20, 30]
it = iter(lst)
print(next(it))
print(next(it))
With generators, you usually dont need iter() since they're already iterators
for i in range(5):
    print(i) # 0 1 2 3 4
typing.Generator
from the typing module, used only for type hints when defining a generator function
def function_name(num_events: int) -> Generator[str, None, None]:
    for i in range(num_events):
        yield f"Event {i+1}"
This doesn't functionality but tells Python that this function is a generator that yield str values



Go crazy:
autopep8 --in-place --aggressive --aggressive ft_garden_management.py
### Instructions

You run this code by doing python3 file_name.py

## Resources

The internet

## AI Usage

Testing my code with test cases and helping me find syntax errors