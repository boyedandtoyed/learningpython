"""import Why
# print("Why")
# import checker
from mr_reload import reload_all
reload_all(Why)
# print("Why")
# import checker
'''
visited = {Why,}
'''

"Later_job"
'''
import Why
'''
Why==
import checker
print("Why?")
from importlib import reload
reload(checker)
'''

print("just Checking")
from importlib import reload

reload(Why)
# four times loop? hmmm...

a = "".maketrans("abcd", "1234")
print(a)
b = {chr(i):chr(65+(((i + 5)-65) % 26)) for i in range (65, 91)}
c = {chr(i):chr(97+(((i + 5)-97) % 26)) for i in range (97, 123)}
print(b.update(c),b)
"""


class Whu:
    def __str__(self):
        print("I'm in.")
        self.s = "78"
        return self.s * 10


class Why(Whu):
    pass


a = Whu
print(a)
a = Whu()
print(a.__dict__, Whu.__dict__)
str(a)
print(a, a.__dict__, Whu.__dict__)
b = Why
print(b, b.__base__, )  # or b.__bases__
b = Why()
print(b)
str(b)
print(Whu.__dict__, ".....................................", Why.__dict__,
      ".....................................", dir(Whu), "....................................."
      , dir(Why),)
