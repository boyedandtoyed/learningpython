a = "I'm in."
from checker1 import X  # OK: "X" already assigned
b = "I'm not in."
from checker1 import Y  # Error: "Y" not yet assigned
print(X, Y)