X = 1
import checker2   # Run checker2 now if it doesn't exist
'''
a = "I'm in."
from checker1 import X  # OK: "X" already assigned
b = "I'm not in."
from checker1 import Y  # Error: "Y" not yet assigned
print(X, Y)
'''
print(checker2.a)
Y = 2
