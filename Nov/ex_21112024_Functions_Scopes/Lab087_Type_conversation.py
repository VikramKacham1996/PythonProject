# Type converstaion
# Type Conversion Examples

a = "10"
print(type(a))  # str

a = int(a)
print(type(a))  # int

a = float(a)
print(type(a))  # float

a = str(a)
print(type(a))  # str

a = bool(a)  # Converts to True (non-empty string or non-zero number)
print(type(a))  # bool

# Convert to list, tuple, and set
a = "10"
a = list(a)
print(type(a))  # list

a = tuple(a)
print(type(a))  # tuple

a = set(a)
print(type(a))  # set

# Convert to frozenset
a = frozenset(a)
print(type(a))  # frozenset

# Example with bytes
a = "10"
a = bytes(a, 'utf-8')  # Encode string to bytes
print(type(a))  # bytes

# Convert to complex
a = "10"
a = complex(a)
print(type(a))  # complex

#int(),str(), flat(),
# bool(), list(), truple(), set(), dict(),
# complex()



# ##########
#
#  chat gpt
# # int()
# a = "10"
# a = int(a)
# print(f"After int(): {a}, Type: {type(a)}")
#
# # str()
# a = 123
# a = str(a)
# print(f"After str(): {a}, Type: {type(a)}")
#
# # float()
# a = "10.5"
# a = float(a)
# print(f"After float(): {a}, Type: {type(a)}")
#
# # bool()
# a = 0
# a = bool(a)
# print(f"After bool(): {a}, Type: {type(a)}")
#
# # list()
# a = "hello"
# a = list(a)
# print(f"After list(): {a}, Type: {type(a)}")
#
# # tuple()
# a = [1, 2, 3]
# a = tuple(a)
# print(f"After tuple(): {a}, Type: {type(a)}")
#
# # set()
# a = "aabbcc"
# a = set(a)
# print(f"After set(): {a}, Type: {type(a)}")
#
# # dict()
# a = [("key1", "value1"), ("key2", "value2")]
# a = dict(a)
# print(f"After dict(): {a}, Type: {type(a)}")
#
# # complex()
# a = "10"
# a = complex(a)
# print(f"After complex(): {a}, Type: {type(a)}")
#





