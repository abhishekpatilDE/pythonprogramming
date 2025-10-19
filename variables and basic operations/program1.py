#Create following types of variables in Python using implicit and explicit declaration and assign values to them and print all the variables with their types

# Implicit declaration of funtions 
x = "Hello, World!"  # String
y = 42               # Integer
z = 3.14             # Float
a = True             # Boolean
b = [1, 2, 3]        # List
c = (4, 5, 6)        # Tuple
d = {7, 8, 9}        # Set
e = {"name": "Alice", "age": 30}  # Dictionary
f = None             # NoneType
g = b'Hello'        # Bytes
h = bytearray(5)    # Bytearray
i = complex(2, 3)   # Complex Number
j = frozenset([10, 11, 12])  # Frozenset
k = range(5)        # Range
l = memoryview(b'Hello')  # Memoryview
m = lambda x: x * 2  # Function
n = (i for i in range(3))  # Generator Expression
o = type(x)         # Type
p = Ellipsis        # Ellipsis

# Explicit declaration of functions
str_var: str = "Hello, World!"  # String
int_var: int = 42               # Integer
float_var: float = 3.14         # Float 
bool_var: bool = True           # Boolean
list_var: list = [1, 2, 3]      # List
tuple_var: tuple = (4, 5, 6)    # Tuple
set_var: set = {7, 8, 9}        # Set

dict_var: dict = {"name": "Alice", "age": 30}  # Dictionary
none_var: type(None) = None     # NoneType
bytes_var: bytes = b'Hello'     # Bytes

bytearray_var: bytearray = bytearray(5)  # Bytearray
complex_var: complex = complex(2, 3)  # Complex Number
frozenset_var: frozenset = frozenset([10, 11,
                                            12])  # Frozenset
range_var: range = range(5)  # Range
memoryview_var: memoryview = memoryview(b'Hello')  # Memoryview
function_var: callable = lambda x: x * 2  # Function
generator_var: type((i for i in range(3))) = (i for i in range(3))  # Generator Expression
type_var: type = type(x)  # Type
ellipsis_var: type(Ellipsis) = Ellipsis  # Ellipsis

# Print variables with their types
variables = [x, y, z, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p,
             str_var, int_var, float_var, bool_var, list_var, tuple_var,
             set_var, dict_var, none_var, bytes_var, bytearray_var,
             complex_var, frozenset_var, range_var, memoryview_var,
             function_var, generator_var, type_var, ellipsis_var]

for var in variables:
    print(f"Value: {var}, Type: {type(var)}")