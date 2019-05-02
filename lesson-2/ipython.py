# coding: utf-8
num = 33333333333333333333333333333333333333333
num
bool(0)
bool(4)
a = bool(4)
a = int('888')
a
a = int('888', 7)
a = int('888', 9)
a
b = ([0,1])
b
b = ([0,1],)
b
hash(b)
try:
    bb
except:
    raise ValueError
    
try:
    bb
except:
    raise ValueError()
    
    
'k' in 'keren'
'o' in 'keren'
'k' not in 'keren'
5 in range(10)
class BiggerThan:
    def __init__(self, n):
        self.n = n
        
class BiggerThan:
    def __init__(self, n):
        self.n = n
    def __eq__(self, other):
        return self.n > other
        
BiggerThan(5) in range(10)
BiggerThan(11) in range(10)
class BiggerThan:
    def __init__(self, n):
        self.n = n
    def __eq__(self, other):
        return self.n < other
        
        
BiggerThan(11) in range(10)
BiggerThan(5) in range(10)
list(range(10))
class BiggerThan:
    def __init__(self, n):
        self.n = n
    def __eq__(self, other):
        print(f"compare {self.n} with {other}")
        return self.n < other
        
        
BiggerThan(11) in range(10)
BiggerThan(5) in range(10)
class BiggerThan(int):
    def __eq__(self, other):
        return self < other
        
n = BiggerThan(5)
n < 6
n > 3
n == 5
n == 9
n == 2
dir(n)
dir(str)
dir(object)
str.__dir__
str.__dir__()
"0".__dir__()
def f():
    pass
    
callable(f)
callable(5)
callable(int)
hasattr('__le__', 5)
hasattr(5. '__le__')
hasattr(5, '__le__')
hasattr(, '__le__')
hasattr(f, '__le__')
hasattr(f, '_iter__')
hasattr(list(), '__iter__')
hasattr(f, '__iter__')
ValueError.mro()
class Root(Exception):
   pass
   
class Left(Root):
    pass
    
class Right(Root):
    pass
    
class Join(Left, Right, int):
    pass
    
class Join(Left, Right):
    pass
    
Join.mro()
help(with)
help("with")
with open(r"C:\Temp\test.txt", mode="w") as f:
    f.write("Hello World")
    
import tempfile
with tempfile.TemporaryDirectory() as tmp_dir:
    pass
    
def f():
    x = 5
    x += 1
    return x
    
f()
f()
f()
def f():
    f.x = 5 if not hasattr(f, 'x') else f.x
    x += 1
    return x
    
f()
def F():
    x = 5
    def f():
        x += 1
        return x
    return f
    
tempfile.__file__
f = F()
f
f()
dir(f)
f.__code__
get_ipython().run_line_magic('cls', '')
x = [i for i in range(10) if i % 2 == 0]
x
x = [i**2 for i in range(10) if i % 2 == 0]
x
d = {}
d = { i: i** 2 for i in range(10) }
d
import pprint
pprint.pprint(d)
get_ipython().run_line_magic('pinfo', 'pprint.pprint')
pprint.pprint(d, iwdth=1)
pprint.pprint(d, width=1)
r = { v: k for k, v in d.items() }
pprint.pprint(r, width=1)
map(lambda i: i*i, range(10))
list(_)
_
_90
filter(lambda i: i*i, range(10))
list(_)
x = 5 if False else 1
x
def sqyare(i):
    return i*i
    
filter(sqyare, range(10))
list(_)
sqyare = lambda i: i* i
sqyare
def override_me():
    print('I should be overriden")
def override_me():
    print('I should be overriden')
    
def constant():
    override_me()
    
constant()
constant()
def new_override():
    print("now I'm overriden")
    
override_me = new_override
constant()
get_ipython().run_line_magic('cls', '')
def one2hundred():
    i = 1
    while i < 100:
        yield i
        i += 1
        
iterator = one2hundred()
iterator
next(iterator)
def one2hundred():
    print('start')
    i = 1
    print('i=1')
    while i < 100:
        print(f'returning i={i}')
        yield i
        print(f'increment i ({i})')
        i += 1
        
        
next(iterator)
next(iterator)
iterator = one2hundred()
iterator
next(iterator)
next(iterator)
next(iterator)
next(iterator)
while True:
    next(iterator)
    
def generate_file():
    f = open()
    yield f
    f.close()
    
for i in range(10):
    for j in range(10):
        print((i, j))
        
def count_i():
    for i in range(10):
        yield i
        
def count_j():
    for j in range(10):
        yield j
        
count_j = count_i
def world():
    yield from range(10)
    
w = world()
next(w)
next(w)
next(w)
get_ipython().run_line_magic('cls', '')
tempfile.__file
tempfile.__file__
import json
json.__file__
json.__version__
import time
time
import time as another_name
another_name
another_name == time
from time import altzone
altzone == another_name.altzone == time.altzone
altzone == another_name.altzone == time.altzone == False 
json.codecs
json.JSON
import logging
logging.config
import logging.config
logging.config
