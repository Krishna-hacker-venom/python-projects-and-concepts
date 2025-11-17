# Create an empty tuple in two different ways.
tuple_1 = () # First way
tuple_2 = tuple() # Second way

# Create a tuple containing mixed data types (int, float, string, bool, list, tuple).
tuple_3 = (22, 1.2, "krishna", True, [1,2,3], (1,2))

# Create a tuple containing only one element and explain why (5) is not a tuple.
tuple_4 = (56,) # (5) is not a tuple because it is interpreted as an integer enclosed in parentheses. The comma is necessary to define a single-element tuple.

# Check the type of (10,) and (10).
tuple_5 = (10,)
tuple_6 = (10)
type(tuple_5) # This will be <class 'tuple'>
type(tuple_6) # This will be <class 'int'>
# Create a tuple using the tuple() constructor.
value = [1, 2, 3, 4]
tuple_7 = tuple(value)

# printing all the tuples
print("Tuple 1:", tuple_1)
print("Tuple 2:", tuple_2)
print("Tuple 3:", tuple_3)      
print("Tuple 4:", tuple_4)
print("Tuple 5:", tuple_5, "Type:", type(tuple_5))
print("Tuple 6:", tuple_6, "Type:", type(tuple_6))
print("Tuple 7:", tuple_7)