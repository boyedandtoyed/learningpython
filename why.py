r"""
n=str(input("Enter the name you admire:"))
print((n).title(),'once didn%st said:"Happiness is more satisfactory than absolute success"'%"'")

import this
k=[1,2,3,4,5]
print(k)
a=k.pop()
print(a)
print (k)
l=['Bishwo', 'Binid', 'Yubin','Som']
k=l.copy()
b=0
for i in k:
 print(i, "I'd like to invite to my birthday party. Hope you'd come!")
 n=input("Enter the name of the person you want to invite in replace of %s:"%str(i))
 l.pop()
 print (i, "won't attend the party. I'd also like to invite you Mr.",n.title())
 l.insert(b,n)
 b=b+1
print (l)

k=["c",'E','A','b','d']
print(sorted(k))
sorted(k)
print(k)
k=[]
for i in range(1,1000001):
    k.append((i))
    print (i)
print (k)
print(sum(k))
k=[]
for i in range(1,11):
    k.append(i**3)
    print (k[i-1])
print(k)

f4rth10=[val**4 for val in range(1,11)]
print(f4rth10) 
k=['banana', 'apple', 'orange', 'litchi','guava']
print (k[1:5]) 
k=[1,2,3,4,5]
l=k.copy()             # l=k 'not gonna work'
k.append(9)
print(l)
print([value**2 for value in range(1,11)])

k=(1,2,3,4,5)
print(k)
for i in k:
    print (i)
if k[0]==1:
 print("f%sk"%"uc")
k ="kera"
print(k != "kera")
k=int(input("enter the thing you wanna store:"))
if k not in [ value for value in range(1,11)]:
    print ("Hey!, you are right. Using", k,"would be amazing.")
else:
    print("use other shits")
print([ value**2 for value in range(1,12)])
k={"k":"ker",
   "ker":4}
print(k["ker"])

# brother challenged me to print numbers without having any number in the program or by having all words and syntaxes
k=["word", "wordo","wordt","wordth","wordf" ]
k.reverse()
for i in k:
    print (k.index(i))

k={"a":1,"b":2,2:3,"d":4,"e":5}
k["b"]="a"
print (k["e"]+k["d"])
print(k[2])

k={"echo":"sound",
   "computer":"electronics",
   "eyes":"vision",
   "pen":"writing",
   "rack":"clothes",
   }
for i,j in k.items():
    print(i+" refortifies:\n",j,"\n")
k=((5,6),
   (4,5),
   (3,4),
   (2,3),
   (1,2),)
for i in k:
    print(i[0],"+ 1 =",i[1])


k=[1,2,3,4,5,6]
for i in range (len(k)):
 k[i]+=1
 print (i+1)
print(k)
user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }
for key, value in user_0.items():
 print("\nKey: " + key)
 print("Value: " + value)
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!"
               
print(""
      ""
      ""
      ""
      "k")

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
programming_languages = favorite_languages.values()
print(programming_languages)
person = favorite_languages.keys()
print(person)

bishwo={"surname":"tiwari","level":"secondary"}
shankhar={"surname":"ghorasaini", "level":"bachelors'"}
people=[bishwo,shankhar]
for person in people:
    print("His surname is:",person["surname"].title()+" and he studies in", person["level"].title(), "school.")

favorite_numbers={
"Hero":[2,5,8],
 "Sharky":[1,4,7],
  "normie":[1]  ,
}
for favorite_number in favorite_numbers:
    list=favorite_numbers[favorite_number]
    length=(len(list))
    if length==1:
        print(favorite_number+"'s favorite number is:")
        for i in range(length):
            print ( "\t",list[i] )
    else:
        print(favorite_number+"'s favorite numbers are:")
        for j in range(length):
            print("\t", list[j])

cities={
    "Kathmandu": {"country_located" : "Nepal",
                 "speciality" : "city of temples",
                 "population": "5000000",
                 },
    "Cairo":    {"country_located" : "Egypt",
                "speciality" : "city of gizmos and pyramids",
                "population": "7000000",
                },
    "New_York": {"country_located" : "USA",
                "speciality" : "it's new york, just kidding the statue thing.",
                "population": "10000000",
                },
}
#for city, city_info in cities.items():
   # print (city,":")
    #print("Country located:", city_info["country_located"])
#    print("Speciality:", city_info["speciality"])
 #   print("Population:", city_info["population"])
#same thing
for city, city_info in cities.items():
    print (city,":")
    for info in city_info:
        print(info,":",city_info[info])

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
sth= True
while sth:
    message = input(prompt)
    if message.lower()=='quit':
        sth=False
    else:
        print(message)
k=["U","N","I",]
p=""
while "F" not in k:
    for l in "CEF":
        k.append(l)
print(k)
for li in k:
    p = p + li
print(p) 

k={}
active=True
while active:
    name = input("enter your name:")
    answer = input("What's your dream vacation?")
    k[name]=answer
    choice=input("Do you still want to add more informations?(yes/no):")
    if choice.lower()=="yes":
        continue
    elif choice.lower()=="no":
        active=False
    else:
        print("please enter either yes or no")
        choice = input("Do you still want to add more informations?(yes/no):")
        if choice.lower() == "yes":
            active = "true"
        elif choice.lower() == "no":
            active = False

for people,place in k.items():
    print (people.title(),"would love to visit",place.title())

def shirt_info(size, printing_message):
    print ("Shirt's size is ",size," and the message ",printing_message.upper()," will be printed.")
i=input("Enter the shirt's size: ")
j=input("Enter the message you wanna enter: ")
shirt_info(printing_message=j,size=i)


def city_country_pair(city, country):
    location_description=("%s ,%s"%(city, country))
    return (location_description)
combination_1= city_country_pair("Kathmandu","Nepal")
combination_2=city_country_pair("Tokyo","Japan")
combination_3= city_country_pair("San Fransisco","USA")
print (combination_1)
print(combination_2)
print(combination_3)

k=True
a=1
album_data={}
def make_album(artist_name, album_title, no_of_tracks=""):

        album_data["Artist's Name"]=artist_name
        album_data["Album's Title"]=album_title
        if no_of_tracks:
            album_data["No of tracks"]= int(no_of_tracks)
        return(album_data)
while k:
        print ("Enter 'q' anywhere for quitting entering data")
        artist_name= (input("Enter artist's name: ").title())
        if artist_name.lower()=='q':
            break
        album_title= (input("Enter album's title: ").title())
        if album_title.lower()=='q':
            k= False
        track_amount=input("Enter the number of tracks in the album if you want to: ")
        if track_amount.strip!="":
            b=make_album(artist_name, album_title, no_of_tracks=(track_amount))
        else:
            b=make_album(artist_name,album_title)
        print (b)



def print_shits(names_of_shits):
    for name_of_shit in names_of_shits:
        print("\nHey %s !, you're a dk."%name_of_shit)
def pleasure_excitement(names_of_shits):
    for great_things in names_of_shits:
        names_of_shits[names_of_shits.index(great_things)]="Great %s"%great_things
    return names_of_shits

names_of_shits = ["I", "Me", "Myself", "Binod", "Tiwari"]
print_shits(names_of_shits[:])
print(pleasure_excitement(names_of_shits[:]))
print(names_of_shits)
'''

'''def make_pizza(*toppings):
    '''Print the list of toppings that have been requested.'''
    for topping in toppings:
        print(topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
'''
'''
def build_profile(first, last, **user_info):
  '''Build a dictionary containing everything we know about a user.'''
  profile = {}
  profile['first_name'] = first
  profile['last_name'] = last
  print(user_info)
  for key, value in user_info.items():
   profile[key] = value
   return profile
user_profile = build_profile('albert', 'einstein',
 location='princeton',
 field='physics')
print(user_profile)

def animals(animal_type, *additional_info):
    print ( "These are the features of your", animal_type, ":" )
    for info in additional_info:
        print(info)
animals("dog","07 years", "19 quadrillion atoms")
animals("cat","06 years", "17 quadrillion atoms","black and brown hybrid colour pathched","green eyes")


def users_info(first_name,last_name, **additional_infos):
    print("Here's everything I know about you: ")
    print("Your name is:", first_name,last_name)
    copied_extended_additional_info ={"first name":first_name, "last name":last_name}
    for key_info, value_info in additional_infos.items():
        print ("Your", key_info,":", value_info)
        copied_extended_additional_info[key_info]=value_info
    print(additional_infos)
    return (copied_extended_additional_info)

first_name="Binod"
last_name="Tiwari"
location="Wotu"
permanent_address="Khadkule"
print(users_info(first_name,last_name, location=location, permanent_address=permanent_address))


from Time import *
fibonnaci_series()
prime_number()


from First_class import *
restaurant_idea1=Restaurant("Episodic", "back park", 18)
restaurant_idea1.restaurant_info()
restaurant_idea1.restaurant_openess()
restaurant_idea2=Restaurant("New Paradise", "Green houses-86", 21)
restaurant_idea2.restaurant_info()
restaurant_idea2.restaurant_openess()
restaurant_idea3=Restaurant("paramin", "yellow stone park", 8)
restaurant_idea3.restaurant_info()
restaurant_idea3.restaurant_openess()

from First_class import *
# By the way I found this after very long.
# The fact that Eric Matthes is the author of the book I am studying.
# And I wrote the name below unconsciously, though Matthews is incorrect.
user1_details= User("Eric", "Matthews", "Bachelors" ,"Computing")
user1_details.greetings()
user1_details.description_of_user()
print(user1_details.first_name)
user2_details=User ("Ramesh","Khatiwada", "Masters", "accounting")
user2_details.greetings()
user2_details.description_of_user()

import First_class
print (First_class.Restaurant.__doc__)
print("my name")
if __name__!="__main__":
    print("a")
else:
    print("no")

class something():
    #self is appropriate but not a compulsion
     def __init__ (false, deal):
         false.deal=deal
         print( false.deal)
p=something("Deal?")
print (p)
              
class idk():
# check
    def __init__(self):
        self.l="deal?"
p=      idk()
print(p.l)

from First_class import Restaurant
_1st_restaurant = Restaurant("Dean'", "Soth palace", 7 )
print(Restaurant("Dean", "Soth palace", 7 ).name)
print(_1st_restaurant.location)
print(_1st_restaurant.time)
_1st_restaurant.restaurant_info()
print(_1st_restaurant.restaurant_openess())
print(_1st_restaurant.number_served)
_1st_restaurant.number_served=10
print(_1st_restaurant.number_served)
numbers_served=int(input("Enter no of total serves: "))

print (_1st_restaurant._numbers_served(numbers_served))
extra_serves=int(input("What's the number of serves today? "))
print(_1st_restaurant._additional_served(extra_serves))


from First_class import User
first_name=input("First Name: ")
last_name=input("Last Name: ")
education_level=input("Education Level: ")
experties_area=input("Experties_area: ")
user_1= User(first_name,last_name, education_level, experties_area)
user_1.greetings()
user_1.description_of_user()
print(user_1.increament_login_attempts())
print(user_1.increament_login_attempts())
print(user_1.login_attempts)
print(user_1.reset_login_attempts())

from First_class import Restaurant
class Ice_cream_stand(Restaurant):
    def __init__(self,name,location,time):
        super().__init__(name,location,time)
        self.flavours=["chocolate","vanilla","strawberry","mango","butter scotch"]

    def display_flavours(self):
        print ("We have following flavours of ice cream: ")
        for flavour in self.flavours:
            print(flavour.title())

Ice_cream_stand1=Ice_cream_stand("Divine","Parking Hotel",8)
(Ice_cream_stand1.restaurant_info())
print(Ice_cream_stand1.restaurant_openess())
(Ice_cream_stand1.display_flavours())
print(Ice_cream_stand1._numbers_served(10))
print(Ice_cream_stand1._additional_served(10))

from First_class import User
class Admin(User):
    def __init__(self,first_name,last_name,education_level, experties_area):
        super().__init__(first_name , last_name , education_level , experties_area)
        self.previlages= ["can accept members","can remove members", "can ban members or users",]
        self.previlages +=["can add posts", "can remove posts"]
    def _show_previlages(self):
        print("Here's what ", self.first_name.title(),self.last_name.title()," can do:")
        for previlage in self.previlages:
            print(self.first_name.title(), self.last_name.title(), previlage,".")


admin_1 = Admin("Sanjay","SapkotA", "MasterS","Electric Batteries")
admin_1.greetings()
admin_1.description_of_user()
admin_1._show_previlages()

from First_class import User
class Previlages():
    def __init__(self,first_name,last_name,education_level,experties_area):
        self.previlages = ["can accept members", "can remove members", "can ban members or users", ]
        self.previlages += ["can add posts", "can remove posts"]
        self.first_name = first_name
        self.last_name = last_name
        self.education_level = education_level
        self.experties_area = experties_area
    def show_previlages(self):
        print("Here's what ", self.first_name.title(), " ",self.last_name.title(), " can do:",sep="")
        for previlage in self.previlages:
            print(self.first_name.title()," ", self.last_name.title()," ", previlage, ".", sep="")

class Admin(User):
    def __init__(self,first_name,last_name,education_level, experties_area):
        super().__init__(first_name , last_name , education_level , experties_area)
        self._previlages_=Previlages(first_name,last_name,education_level,experties_area)

admin_1 = Admin("Sanjay","SapkotA", "MasterS","Electric Batteries")
admin_1.greetings()
admin_1.description_of_user()
admin_1._previlages_.show_previlages()

class Car():
    '''A simple attempt to represent a car.'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery():
    '''A simple attempt to model a battery for an electric car.'''

    def __init__(self, battery_size=70):
        '''Initialize the battery's attributes.'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''Print a statement describing the battery size.'''
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    def upgrade_battery(self):
        '''Upgrade battery size into 85'''
        if self.battery_size!=85:
            self.battery_size=85

    def get_range(self):
        '''Print a statement about the range this battery provides.'''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
class ElectricCar(Car):
    '''Represent aspects of a car, specific to electric vehicles.'''

    def __init__(self, make, model, year):
        '''Initialize attributes of the parent class.'''
        super().__init__(make, model, year)
        self.battery=Battery()
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


from First_class import User,Previlages,Admin

admin_1 = Admin("Sanjay","SapkotA", "MasterS","Electric Batteries")
admin_1.greetings()
admin_1.description_of_user()
admin_1._previlages_.show_previlages()

from random import randint
x=randint(1,12)
print(x)

with open('Nothing.txt') as nothing:
    questions=nothing.read()
    print(nothing.readable())
    print (questions)
k ="Whatever
      happens
      I'll
      go
      to hell.
     "
for i in k:
    print (i,end='')

file_path="Nothing.txt"
with open(file_path) as file:
    for p in file:
        print (p.rstrip())
  
file_path="Nothing.txt"
with open(file_path) as something:
    lines=something.readlines()
    for line in lines:
        print (line.rstrip())
print(lines)

file_path="New thing.txt"
with open(file_path) as anything:
    for data in anything:
        print (anything)

first="something"
second="nothing"
print("{1} is better than {0}".format(second,first))

print('{0:.54}'.format(1/3))
print("{0:*^12}".format("Yeah"))
print(1/3)

import os

print(os.getcwd())

import First_class
print(dir(First_class))

a=5
print (vars())

n="BinodTiwari"
shoplist = set(['apple', 'mango', 'carrot', 'banana'])
list=['apple', 'mango', 'carrot', 'banana']
k=shoplist.copy()
k.add("litchi")
print(shoplist.issubset(k))
print(k&shoplist)
print(k.intersection(shoplist))
print(shoplist.intersection(k))
delimiter1=" fruit\n"
delimiter2="- Character\n"
print(delimiter1.join(list))
print(delimiter1.join(shoplist))
print(delimiter2.join(n))
print(n.find("24132536457"))
print(n.startswith("Bin"))

#there is a book mark function just press
#ctrl shift and the number or ctrl f11
#something is fishy.
k="Nothing.txt"
with open(k) as something:
    m=list(something)
    n=something.readlines()
    print (m)
    print (n)
    for l in something:
        print (l)

#just checking, not gonna work
k="Nothing.txt"
with open(k) as something:
    print (something[])


k="Nothing.txt"
with open(k,"r+") as something:
    a=something.read()
    print(a.replace("mad","sexy"))
    print(a)

b="You're so " \
  "so " \
  "so " \
  "so " \
  "dead."
print (b)
print(b.replace("dead","cute"))
print (b)

k="New thing.txt"
with open(k,"r+") as something:
    something.write("Python is something ridiculous thought, a thought that is never a change " 
                    "but always an image.")
    something.write("\nSomething is going wrong, will it work?")
    a=something.read()
    print (a)

a="I like you"
l=a.split()
print (l,a)

a='C:/Users/Hp/Documents/INDEPENDENCE.txt'
with open(a,"r") as something:
    b=something.read()
    print(b)

a= True
while a:
    try:
        # a=False is not gonna work here
        a=int(input("Enter any 1st number:"))
        b=int(input("Enter any 2nd number:"))
        print(float(a)/float(b))
        #It'll work here
        a = False
    except  ValueError as wut:
        print("Please enter integers or any real numbers only.")
    except ZeroDivisionError as g:
        print("Denominators can't be zero")

a="Everything.txt"
try:
    with open(a) as fine:
        b=fine.read()
        print (b)
except FileNotFoundError:
    print("Sorry, there are no files named",a,"in the given location.")

a="Nothing.txt"
try:
    with open(a) as fine:
        b=fine.readlines()
        print (b)
except FileNotFoundError:
    pass

a="My name is Binod Tiwari and his name is Bishwo mani tiwari"
print(a.lower().count("name"))
print(a.lower().count("tiwari"))

import json
a="New thing.txt"
users_fav_number=input("Enter your favourite number: ")
with open(a,"w") as something:
    json.dump(int(users_fav_number),something)

with open(a,"r") as nothing:
    print(json.load(nothing))

import json

a = "New thing.txt"
try:
    with open(a, "r") as anything:
            print(json.load(anything))

except FileNotFoundError:
    with open(a, "w") as anything:
        users_fav_number = input("Enter your favourite number: ")

        json.dump(int(users_fav_number), anything)

#Just some Bullshit
import json
global f
f="New thing.txt"
def new_user_assign():
    print("So, you're the new user:")
    b=input("Enter your name: ")
    with open (f,"w") as anything:
        json.dump(b,anything)
def  get_old_user_name():
    try:
        with open(f) as something:
            username=json.load(something)
            print("Is your name", username, "?")
            a = input("Enter Y for yes and N for no: ")
        if a.lower()=="y":
            return username
        elif a.lower()=="n":
            return (new_user_assign())
    except FileNotFoundError:
        pass
def get_new_user_name():
    with open (f) as right_thing:
        return (json.load(right_thing))
def greet_user():
    if get_old_user_name():
        print("So, you've returned", get_old_user_name())
    elif get_new_user_name():
        print("We'll remember you", get_new_user_name(),"next time around.")
    else:
        with open(f,"w") as wrong_thing:
            c=input("Enter your name: ")
            json.dump(c,wrong_thing)
            print("Thanks for assigning,",c)
greet_user()
#Upto here

import json
global f
f="New Thing.txt"
def load_an_existing_name():
    #Loads a name if it exists.
    with open(f) as nothing:
        user_name=json.load(nothing)
    return (user_name)
def create_a_file_or_input_new_name(user_name):
    #creates a file in need, dumps a name otherwise.
    with open (f,"w") as anything:
        json.dump(user_name.title(),anything)
        return user_name.title()
def open_or_create_file():
    #    a calling function dedicated for printing
     #the name of the user somehow after storing
     #it in a newly or oldly formed file.
    try:
        print("Is your name", load_an_existing_name(), "?")
        answer = input("Enter Y for yes and N for no: ")
        if answer.lower().strip()=="y":
            print("So you've returned",load_an_existing_name())
        elif answer.lower().strip()=="n":
            print ("So you're new user:")
            user_name = input("Enter your name: ")
            create_a_file_or_input_new_name(user_name)
            print("We'll remember you next time",user_name.title())
        else:
            print("Please enter either y or n")
            open_or_create_file()
    except FileNotFoundError:
        user_name = input("Enter your name: ")
        create_a_file_or_input_new_name(user_name)
        print("You're our first user. We'll remember you next time", user_name.title())
open_or_create_file()
#This program gave it "satisfaction". 

import unittest
from Just_something import names
from  Just_something import Name_Test

unittest.main()

#supposed to be in a file test_city.py module
import unittest
from city_functions import city_country_data
class Country_data_Test(unittest.TestCase):
        def test_city_country(self):
            returned_data=city_country_data("Hetauda","NePaL")
            self.assertEqual(returned_data,"Hetauda, Nepal")
            print(returned_data)
        def test_city_country_population(self):
            returned_data=city_country_data("Delhi", "InDiA",150000000)
            self.assertEqual(returned_data,"Delhi, India:Population- 150000000")
            print(returned_data)
unittest.main()
Country_data_Test.test_city_country()

import os
print(os.getcwd())

import sys
print(sys.platform)

import First_class
a=dir(First_class)
print(a)
#classes come first, then functions
# then builtin interpreter function then comes variables.
import Bishwo
b=dir(Bishwo)
print(b)

a="idea"
b=a.partition("d")
print (b)
c=list(b)
print(c)
c[2]=c[2].split()
print(c)

l=[1,2,3]
p=[2,3,4]
p.append(l)
print(p)
l.append(l)
print(l)
#print(2**50000)

k=b"fdzcxvcb" #wth
print(k)
k=1+3j #wth
print(k**2)
k=5
print(k%2)
print(7//3)
print(len(str(2**500000)))

import random
print(random.choice([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
import math
print (math.pi)
a="Pine"
print(a[1:3])
a=[1,2,3]
a=a+[2]
print(a)
#same thing polymorphism
a=[1,2,3]
a.append(2)
print(a)
a="Nine"
print(a[0:-1])
a="ab,c,d,e"
print(a.split(",",2))
a="abcdefghij k.ghfd"
print(a.split(" "  or "."))
print(a.isascii())
print(dir(a))

a="Ask me a question."
print(a.replace("e","o",1))
print(a)
print(ord("9"))
a="A0 \000\n"
print(len(a))
print(a)
print(r"dfbdfbv'fgbvc\\\\\\\n")
msg = r'''aaaaaaaaaaaaa/////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#bbb#bbbbbbbbbb""bbbbbbb'bbbb
#cccccccccccccc'''
print(msg)
'''
# just for fun
# put an r and remove an r and see outputs on both cases
sth = r'''
                             /\
                            //\\
                           ///\\\
                          ////\\\\
                         /////\\\\\
                        //////\\\\\\
                       ///////\\\\\\\
                      ////////\\\\\\\\
                     /////////\\\\\\\\\
                    //////////\\\\\\\\\\
                   ///////////\\\\\\\\\\\
                  ////////////\\\\\\\\\\\\
                 /////////////\\\\\\\\\\\\\
                //////////////\\\\\\\\\\\\\\
               ///////////////\\\\\\\\\\\\\\\
              ////////////////\\\\\\\\\\\\\\\\
             /////////////////\\\\\\\\\\\\\\\\\
            //////////////////\\\\\\\\\\\\\\\\\\
           ///////////////////\\\\\\\\\\\\\\\\\\\
          ////////////////////\\\\\\\\\\\\\\\\\\\\
         /////////////////////\\\\\\\\\\\\\\\\\\\\\
        //////////////////////\\\\\\\\\\\\\\\\\\\\\\
       ///////////////////////\\\\\\\\\\\\\\\\\\\\\\\
      ////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\
     /////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\
    //////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\
   ///////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\
  ////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\
 /////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
//////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
'''
#just for fun ends
print(sth)
print("Ab\100")

import re
match = re.match('Hello[\t]*(.*)world','Hello\tPython world')
print(match.group(1))
help(re.match)
match = re.match('/(.*)/(.*)/(.*)', '/usr/home/lumberjack')
print(match.groups())

l=["a","z","A"]
print(l)
l.sort()
print(l)
l.reverse()
print(l)
# just sth that doesn't work l.reverse().sort()

#NumPy is powerful, maybe equivalent to MATLAB systems.
#List comprehensions are really powerful
l=[[1,2,3],
   [4,5,6],
   [7,8,9]]
k=[n for n in range(10)]
print(l)
print(k)
column2=[d[1] for d in l]
print(column2)
odd_ones_out=[d for d in column2 if d%2==0]
print(odd_ones_out)
diagonals=[l[n][n] for n in range(len(l))]
print(diagonals)
#comprehension in small brackets builds a generator
#which give values on demands , for e.g.
a=(l for l in l)
print(next(a))
print(next(a))
#lets see what map does
s=set(map(sum,l))
print(s)
b={}
value=b.get("x",99990)
print(value)
print(b)

a=9,3,5352,443,3,4,5,3,3,3,12,3,9,443
b=[1,2,3,4,5,6,1,2,3,12,34,54]
print(a)
print(b.count(34))
print(a.index(12))
c=(1,"a",[1,2,3])
print(c)
print(c[2][1])
c[2][1]=4
print(c)
c[2].append("I seem mutable enough though.")
print(c)

a={1:4,2:8,3:8,4:8,}
b=a.get(5,None)
print(b)
print(not b)

a=open("Nothing.txt")
print(a.readline().strip())

a.seek(4)
print(a.readline())
print(a.readline().strip())
a.seek(30)
print(len(a.readline()))
#ok I get it what seek does........

#gonna check if it works in strings
a="abcd"
print (a)
print(a.seek(1))
#no sorry thank,you.

import decimal
c=decimal.Decimal(1.33441)# using"1.33441" inside quotations gives accurracy
print(c)
import fractions
a=fractions.Fraction(1,2)
print(a)
print(1.33441)
print(1/3)
print((2/3) + (1/2))
b=fractions.Fraction(2,3)+fractions.Fraction(1,2)
print(b)
e=float(7/6)
print(e)
decimal.getcontext().prec=40
print(decimal.Decimal(7)/decimal.Decimal(6))

a=9
print(isinstance(str(a),str))

import decimal
decimal.getcontext().prec=40
print(decimal.Decimal(13.548697086767654324243657))
print(13.548697086767654324243657)

a=0b101
print(a)
b=complex(5+7j)
print(b)
c=bin(0x7)
print(c)

import random
print(random.randint(1,6))

a=0o673421
print(a.bit_length())
b=(3.4)
print(b.as_integer_ratio())
print(b.is_integer())
print(2251799813685248*3.4)

print(1011<<2)
print(1&101)

a={1,2,3,4,5,6}
b={3,4,5,6,7,8}
print(a^b)

a= [lambda x : x**3,lambda x:x**2-1]
print(a[0](3))
print(a[1](2))

def something(a):
    for i in range(a):
        yield i**2

b=something(8)
print(b)
print(next(b))
print(next(b))
print(next(b))
print(next(something(5)))
print(next(something(5)))
print(something(4))

a={12:4,34:5,45:6}
b={12:4,334:56}
print(a)
print(len(a))
print(len(a)<len(b))

print("%f"%(8.99))
print(3.0==3)

print(round(36.500001))

import sys
print(sys.platform)

print(oct(0b101))
print(int("0o45",8))

l=[1,2,3]
print(l)
del l[2]
print(l)
eval("del l") #WHY ISn't it?
print(l)
eval("l=[1,2,3]") #just why?
print (l)

print("{0:3o}{1:3x}{2:6b}".format(16,16,16))
print("%X, %x, %X" %(255,255,3254364))

l=['1','3','5','7']
a="-".join(l)
print(a)
a="You are the King."
print(a.split(" "))
a="a,b,c,d"
b=a.split(",",2)
print (b)

b=0xFFFFFFFFFFFFFFFFFFFFFFFFFFFF
print(b)
print(bin(b))

print(111111&1)
print(2==0b010)
print(bool(bin(0b1000&0b1001)))
print(bin(0b111+0b1001))
#let's see wtf happened

import math
print(math.pi)
print(math.cos(math.pi))

print(bin(0b11000|0b100))
print(bin(0b1001&0b1110))
#I freaking got it,look at individualities.

import math
print(math.sin(math.pi))
print(0.1+.1+.1-.3)# python mi-steaKES?

import decimal
print(decimal.Decimal.from_float(1.35))# always????
print(1/7)
print(decimal.Decimal("1")/decimal.Decimal("7"))
decimal.getcontext().prec=2
print(decimal.Decimal(1)/decimal.Decimal(3))
print(1/6)
print(decimal.Decimal(1)/decimal.Decimal(6))

import decimal
with decimal.localcontext() as heri:
    heri.prec=2
    print(decimal.Decimal(1) / decimal.Decimal(6))
#decimal.localcontext().prec=2 is wrong

import fractions
print(fractions.Fraction(1.75))#smooth feature.

import fractions
a=2.6
a=fractions.Fraction(*(a).as_integer_ratio())
print(a)
a=a.limit_denominator(300)
print(a)

a=set("abc de")
print(a)
b=set("acd ")
print(b<a)
print(b|a)
print(b&a)
print(a^b)
print(a-b)
print(a^b==(a-b))

a={1,2,3,4,"f"}
print(a)
a.add("f")
print(a)
a.add("e")
print(a)
a.update([1,2,3,4,5,6,7,8,"a","b","c","d","e","f"])
print(a)
b={1,2,3,4,5,6,7,8,}
c={5,6,9,10}
a.symmetric_difference_update(c)
print(a, b, c)  # a={1,2,3,4,7,8,9,10,'a','b','c','d','e','f'}
a.difference_update(b)
print(a, b)  # a={9,10,"a"-->"f"}
print(a.symmetric_difference(c))
print(a ^ c, c ^ a)
print((a-c) | (c-a))
print(a.issubset((range(-100,100))))
print(c.issubset(range(-1000 , 1000)))

a={1,2,3,4,5}
b={2,3,4}
b=frozenset(b)
a.add((b))
print(a)
for c in a:
    print (c)

a=[1,2,3,4,5,6,7,8]
for i in a:
    a.append(i+8)
    print("binod") #infinite loop from a for/

print(int("1010101",2))
print(eval("1010101"))

import copy
a={1:[1,2,3],2:(2,4,6),3:{3:[3,6,9],6:(6,12,18),9:{9,18,27}}}
b=copy.copy(a)
print(a,b)
# More nesting required for deepcopy...or maybe dictionaries...

a=1
b=a
print(a == b, a is b, a, b)
c=1
print(a is c)
a=2
print (a,b,c)
print(b is c)

import sys
print(sys.getrefcount(10))

a="spam"
b=a
b="shruberry"
print(a)

a="s\np\ta\x00m"
print(a)

a = [[1, 2, 3, ], [4, 5, 6], [7, 8, 9]]
b = map(sum, a)
c = list(b)                          # forced b
print(c)
a=b"dsfg"
print(a)

a="s\x01a\fggg"
print(a)
print(bin(122))
a="\01\03\x09"
print(a)
a=("dfghfg" "erstrdfg" "trjgh" "atrsdyfjgh"
"tdfhg" "strdytfygj")
print(a)

a = 10
print(hex(a))
a=0o773
print(bin(a))
a="po\377"
print(len(a))

a="\fpodfg"   #what's a formfeed?
print(a)

a=r"\sfh\jfgdb\bfndgfba\/"[:-1]
print(a)

a=ord("1")
print(hex(a))

print(str("52"),repr("52"))
for i in range (151):
    print(str(i),"-",chr(i))

a=["1","2","3","4","5","6"]
b="123456"
d=list(b)
c="".join(a)
print(c==b)
print(c)
print(d)

# string methods now
a = "ABCDEFGHIJKLM,NOPQRSTUVWXYZ"
b= "aabbcccddddeeeeefffffghhdtlfyryi;pyioohjfihytrafwdgngrshdtkjjplkewtqrdasfvghcjmv,nbbdsghdsjrkdtyluyoirueytwqrdcvcvnf"
print(a.capitalize(), a)   # string never changes
print(a.rjust(44,"F"),a)    # or ljust()
print(a.center(30,"_"),a)
print(b.count("f"), a, b)
c="ABCD"
d="1234"
e=c.maketrans(c, d, "C")  # cute
print(e)
f="AABBCCD"
print(f.translate(e))  # thank you {gives-->(11224)}
print(b.partition(","))  # creates a tuple including the comma as object
print(b.rpartition(","))  # now what's the difference bet_n r and no r, maybe raw strings
g="\txvdbng\t\nbbbb"
print(g.expandtabs(1))  # not exactly expands, contracts too.
print(c.find("C", 1, 3))
print(g.find("n"), g.rfind("n", 5, -1))
print(a.split(","))
print(a.rsplit(",",0))
print(a.isidentifier())
h="675"
print(dir(str))
help(a.format)

# i=#'''  # you are
#    kjhjknlm
# kjhgmknjbh
# jkhg,k
'''
print(h.zfill(7))
print(i.splitlines(True)) # not awesome
print(b.casefold())
# string story almost end...

import string          # functions which aren't methods
s = "1234,bBCD,lnkbjghfgdfd"
print(string.capwords(s, ","))
help(string.Formatter)
print(string.Formatter.format(s,))
# left it f0r later use

a = 1.98734579
b = "%*.*e,%5.4f,%4.*g " % (25,4,a, a, 3, a,)  # using %r gives quotes
print(b)
c = "%(1)5.4f" % {"1": 2.9999}   # I'm the map
print(c)
print('{motto}, {0},{1} and {food}{2}'.format(42, 2, 4, motto=3.14,  food=[1, 2]))

import sys
a= 'My {ok[spam]}{ok[dyam]} runs {not_ok.platform}.'.format(not_ok=sys, ok={'spam': 'laptop',"dyam":1})
print(a)
b="456\radsfsgdnfgc"
print(b)
x = 1234
res = "%(newthing)d" % {"newthing" :x}
print(res)
somelist = list('SPAM')
parts= somelist[0], somelist[-1], somelist[1:3]
print(parts)'
print('first={0}, last={1}, middle={2}'.format(*parts))
print("{0!a:}".format(1))
print('{0:11}={1:<10.0f} or{2:9.0f}'.format('spam', 123.4567, 123.45E+1))
print('{0[hero]:}'.format({"hero":8}))
print('{[hero]}{[hero]}'.format({"hero":8},{"hero":7}))
help('FORMATTING')
print('{0:?^88}'.format("Hello, it's me. I'm in california dreaming about who we used to be."))
print('{0:,}'.format(12345))
print("{:=+24.6f}".format(122.8768))
help("FORMATTING")
import datetime
print(datetime.datetime(1999, 7, 6,))
print("{:3>+25.2f},{:n},{:.3%}".format(2.3, 34535,1520/1600))
print(bin(2**16))

print("{:.15g}".format(1234.2125339345))
a=[1,2,3,4]
print(a*3)
b=[1, 2, 3, 4]
print(a is b)
b.extend(["yy", "noodles", 1])
print(b)
print(b.count("noodles"))
print(b.index(1,))
c = ["fo", "co", "iro", "ao", "Jo", "bo"]
c.sort()
print(c)
b[len(b):]=[5]               # unuse of : generates error
print(b)
print(c)
c.sort(key=str.lower)      # key is a mystery
print(c)

# dicts
a = dict(zip([1,2,3,4,5],["a","b","c","d","e","f"]))  # f gets ignored
print(a)
b=a.fromkeys([1,2,3,4,5],["f","g","h","i","j"])  # yuck its a mess, didn't work as thought
print(b)
print(a.get(5,))
table={"Python": 'Guido Van Rossum',
       'Perl': 'Larry Wall',
       'Tcl': 'John Ousterhout'}
for lang in table:
    print(lang+ " \t " + table[lang])  # how do these arrange themselves
a.setdefault(1, "c")
print(a)
print("r\tt")
a.update(table)
print(a)

# tuples
T = (1, 2, 3, 2, 4, 2,2,3,4,5,3,1,5,)
print(T.index(1,1))

# files...........................?
with open("Nothing.txt") as dictator:
    data = dictator.read()   # n represents the no. of characters inside read method
    print(data)
with open("New Thing.txt", "r+") as dictator1:
    data = dictator1.read()
    print(data)
    dictator1.write("hello\nno hellos\nHi\nNo His\n" )
    print(dictator1.read())
with open("New Thing.txt", "r",) as dictator2:
    data=dictator2.readlines()
    print(data)
for i in open("New Thing.txt"):
    print(i,end="")
a = "hi world"
import pickle
b=open("Goodfile.pkl", "wb")
pickle.dump(a,b)
b.close()
b =open("Goodfile.pkl","rb")
c = b.read()
print (c)
b.close()

a=bytearray("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "utf-8")
print(a)
for i in a:
    print(i)
a.decode("ascii")
print(a)
b = 9
c=bytes(b)
print(c)
print()

print(ascii("urdlsvm-\fdf"), ord("\f"), repr("urdlsvm-\fdf"))
a="{0:b}".format(14)
print(a)
print(f"{10:x}{11:o}.....................{13:.3f}")  # value:format_spec

import datetime
d = datetime.datetime(2010, 7, 6, 12, 15, 58)
print('{0: %Y-%m-%d %H:%M:%S}'.format(d))
print(chr(66)+chr(73)+chr(78)+chr(79)+chr(68))

l = [1, 2, 3, 4]
# print(l[4])
# l[4] = 3
print(l[-1000000:3])
l[3:1] = [0, 9]
print(l)
del(l[3:5])
print(l)
l[2] = []
print(l)
l[2:4]=[]
print(l)
x, y = 3, 4
x, y = y, x
print(x, y)
S = "spam"
print(S[1][0][0][0][0])

def w(p):
    for i in p:
        yield i**2


a = w([1, 2, 3, 4, 5])
print(next(a))
print(next(a))
print(1 & 2)
X, Y = 3, 4
assert X > Y, 1

a, b, c, d = "abcd"
print(a, b, c, d)
e, *f = "NIcething"
print(e, f)
# doesn't work g=dict([1,2,3,4]=[2,3,4,5])
[g, h, i, j]="2345"
print(g, i, h, j)
print(hex(id(f)))
f = [1, 2, 3, 4, 5]
a, b, *c, d = f   # two starred assignment doesn't work, silly
print(a, b, c, d)
print(0xf2)

print("My name is binod binod ki jawani teri hat na aani."
      , file = open("New Thing.txt","w"))    # It works

a, b = 2, 3
print(bin(a), bin(b), bin(a or b), a, b, a or b)
import re
a = re.match("k(.*)k(.*)","kicker")
print(a, a.group(2), a.groups())
a = "sthodfdfreggrfecdwxs"
print(set(a))

file = open("New Thing.txt")
while True:
    char = file.read(1)  # Read by character
    a = file.read(2)
    print(a, end="")
    if not char: break
    print(char, end="")

file = open("anything_new.txt", "rb")
b = file.read(2)
c = file.read(2)
print(b)
print(c)

file = open("anything_new.txt")
while True:
    first = file.read(1)
    second = file.read(2)
    print(second, end="")

    if not first: break
    print(first, end="")
file.close()

import sys
print(sys.path)
file = open("E:/Lovelace books/Hello.exe", "w")
c = file.write("1")
file.close()
file = open("E:/Lovelace books/Hello.exe", "r")
a = file.read()
print(a)
file.close()
print(0, file=open("E:/Lovelace books/Hello.exe", 'w'))

import os
p = (os.popen("dir"))
for i in p:
    print(p)
for i in enumerate("hi notional candidate"):
    print(i)

import operator
print(list(map(operator.add(), [1, 2, 3, 4], [5, 6, 7, 8])))  # wrong

X = (1, 2, 3)
Y = 3, 4, 5
C = list((X, Y))
print(C)
E = zip(X, Y)
print(list(E))
B = zip(*zip(X, Y))
print(list(B))

X = 5
L = map(lambda x: 2 ** x, range(7))  # or [2**x for x in range(7)]
print(L)  # list() to print all in 3.0, not 2.6
if (2 ** X) in L:
    print((2 ** X), "was found somewhere")
else:
    print(X, 'not found')
a = lambda x: x ** 3
print(a(3))

print(0b11 ^ 0b110)
a, b = {1, 2, 3, 4, 5}, {4, 5, 6, 7, 9}
print(a ^ b)
print(8 * "Nnnnnn" * 8 * 9)
if __name__ == '__main__':
    print("hi")
    print(__name__)
print(dir())
import Bishwo
import sys
print(sys.modules["Bishwo"])

def intersect(*args):
    res = []
    for x in args[0]:       # Scan first sequence
        for other in args[1:]:       # For all other args
            if x not in other:
                break       # Item in each one?
        else:            # No: break out of loop
        res.append(x)           # Yes: add items to end
    return res
print(intersect([1, 2, 3, 4, 5, 6],[2, 3, 4, 5, 6, 7],[2, 3, 4, 5, 6]))
print(1, 2, 3, 4, 5)

def my_sum(L):
    return L[0] if len(L) == 1 else L[0] + my_sum(L[1:])
print(my_sum([1,2]))

import sys
showall = lambda x: list(map(sys.stdout.write, x))  # Use list in 3.0
t = showall(['spam\n', 'toast\n', 'eggs\n'])
print(t)

import sys
x = ['spam\n', 'toast\n', 'eggs\n']
k = (map(sys.stdout.write, x))
print(k)
for sth in k:
    print(sth)

import sys
from tkinter import Button, mainloop  # Tkinter in 2.6

x = Button(
    text='Press me' + u"\u00b0",
    command=(lambda: sys.stdout.write('Spam\n')))
x.pack()
mainloop()

def kk(x,y):
    return x-y
print(list(map(kk,[1,2,3,4,5],[9,3,4,5,6,7])))

from functools import reduce
print(reduce((lambda x, y: x*y), [1, 2, 3, 4]))


def zip_(*iterables):  # Accept any iterable, any amount of iterable and return and be exhausted after it's one usage.
    My_iterable_list = list(map(iter, iterables))  # A map object which turns iterables into iterators
    while My_iterable_list:  # loop through the map object
        a = [next(iterings) for iterings in My_iterable_list]
        yield a


return_value = zip_([1, 2, 3, 4], [5, 6, 7, 8])
print(return_value)


def something():
    a = ("k", "a", "s", "m")
    for i in a:
        k = yield i
        print(3 * k)


b = something()
print(b.__next__())
print(b.send(2), b.send(3))


def hero(a):
    print(a)


from time import  clock

reps = 1000
repslist = range(reps)


def timer(func, *pargs, **kargs):
    start = clock()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = clock() - start
    return elapsed, ret


timer(hero, "wut?")
import sys  # Import timer function

reps = 10000
repslist = range(reps)  # Hoist range out in 2.6


def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res


def listComp():
    return [abs(x) for x in repslist]


def mapCall():
    return list(map(abs, repslist))  # Use list in 3.0 only


def genExpr():
    return list(abs(x) for x in repslist)  # list forces results


def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
            return list(gen())


print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    elapsed, result = timer(test)
    print('-' * 33)
    print('%-9s: %.5f => [%s...%s]' %
          (test.__name__, elapsed, result[0], result[-1]))

import this
s = "Fvzcyr vf orggre guna pbzcyrk."
d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

print("".join([d.get(c, c) for c in s]))
print(d)

def saver(x=[]):  # Saves away a list object

    x.append(1)  # Changes same object each time!
    print(x)


saver([2])
saver([2])
saver()
saver()

import time
from imp import reload  # depreciated in 3.8.3
reload(time)
from importlib import reload    # appreciated
reload(time)
print(time.localtime(9))

import sys
print(sys.path)
import Hero
import fractions
a = 3.
b = fractions.Fraction(a)
c = fractions.Fraction(b)
print(c)
import Bishwo as d
print(d.__name__)
print(sys.argv)

def commas(N):
    '''
    format positive integer-like N for display with
    commas between digit groupings: xxx,yyy,zzz
    '''
    digits = str(N)
    assert(digits.isdigit())
    result = ''
    while digits:
        digits, last3 = digits[:-3], digits[-3:]
        result = (last3 + ',' + result) if result else last3
    return result
def money(N, width=0):
    sign = '-' if N < 0 else ''
    N = abs(N)
    whole = commas(int(N))
    fract = ('%.2f' % N)[-2:]
    format = '%s%s.%s' % (sign, whole, fract)
    return '$%*s' % (width, format)
import sys
if __name__ == '__main__':
    def selftest():
        tests = 0, 1 # fails: −1, 1.23
        tests += 12, 123, 1234, 12345, 123456, 1234567
        tests += 2 ** 32, 2 ** 100
        for test in tests:
            print(commas(test))
    print('')
    tests = 0, 1, -1, 1.23, 1., 1.2, 3.14159
    tests += 12.34, 12.344, 12.345, 12.346
    tests += 2 ** 32, (2 ** 32 + .2345)
    tests += 1.2345, 1.2, 0.2345
    tests += -1.2345, -1.2,  -0.2345
    tests += -(2 ** 32), -(2 ** 32 + .2345)
    tests += (2 ** 100), -(2 ** 100)
    for test in tests:
        print('%s [%s]' % (money(test, 17), test))
    if len(sys.argv) == 1:
        selftest()
    else:
        print(money(float(sys.argv[1]), int(sys.argv[2])))

print(sys.argv)
print(int(sys.argv[2]))

import Timely, types
print(getattr(Timely, "fibonacci_series"), Timely.__name__, Timely.__file__)
print(dir(Timely), Timely.__dict__)
print(Timely.city_functions)
print(Timely.__dict__)
for key, attrobj in Timely.__dict__.items():  # For all attrs
    if type(attrobj) == types.ModuleType:  # Recur if module
        print(attrobj, "....", attrobj.__file__)

import sys

print(sys.argv)  # 1
import Why
from mr_reload import reload_all

reload_all(Why)

print("Why")
import checker
#from mr_reload import reload_all
#reload_all(checker)

import checker
print("Why?")
from importlib import reload
reload(checker)

import checker2

class Sth:
    pass


a = Sth()
print(type(Sth), type(a))

a = [1, 2, 3, 4, 5]
print(6 not in a)  # or not 6 in a


def sth():
    pass


print(type(sth), type(sth()))

class Something:
    pass
a = Something()
a.s = "p"
Something()
print(type(a.s), type(a))

a = "Ibqqz Cjsuiebz up nf."
b = [chr(x) for x in range(65, 91)]
c = [chr(x) for x in range(97, 123)]
b = b + c
for letts in a:
    if letts in b:
        print(chr(ord(letts)-1), end="")
    else:
        print(letts, end="")

class Test:

    def __str__(self):
        self.sth = "a"
        print("?")
        return "Wisdom."

    def __add__(self, other):
        print(other)
        return self.sth + other


a = Test()
print(str(a))
b = a + "yy"
print(b)

my_saying = "Mfuud Gnwymifd Yt Rj."
a = {i+65: chr(65 + (i - 5) % 26) for i in range(26)}
print(a)
b = {i+97: chr(97 + (i - 5) % 26) for i in range(26)}
a.update(b)
print(a)
print(my_saying.translate(a))

say = "Mfuud Gnwymifd Yt Rj."
a = {i+65: chr(65 + (i - 5) % 26) for i in range(26)}
b = {i+97: chr(97 + (i - 5) % 26) for i in range(26)}
a.update(b)
print(say.translate(a))

inputFile = open(r"C:\Users\Hp\Desktop\WI.jpg", 'rb')
outputFile = open(r"C:\Users\Hp\Desktop\Hello.jpg", 'wb')
msg = inputFile.readlines()
for i in range(10):
    outputFile.write(msg[i])
inputFile.close()
outputFile.close()

a = int(input("Enter the number: "))
c = ""
while a:
    if a % 2 == 0:          decimal into binary
        b = 0
        a = a // 2
    elif a % 2 == 1:
        b = 1
        a = a // 2
    c = str(b) + c
print(c)

class Sithless:
    def __init__(self, blame, shame):
        self.shame = shame
        self.blame = blame

    def __str__(self):
        self.aerobic = "abd"
        return "Actually that's fine Mr. " + self.aerobic.title()


class Sith:
    '''
    does literally nothing
    '''

    def __init__(self, blame, shame):
        self.s = Sithless(blame, shame)

    def __getattr__(self, item):
        return getattr(self.s, item)


a = Sith
print(a, Sith, type)
a = Sith("Hey!", "Oh,no!")
print(a, type(a))
print(a)
print(a.blame, a.shame, a.__class__, list(a.__dict__.keys()))
for i in a.__dict__:
    print("---------------------------------")
    print(i, "--->\t", getattr(a, i))
    print("---------------------------------")
print("---------------------------------")
print(a.__dict__)

print(a)

import shelve
dm = shelve.open("Somedbm")
dm["Nepali2"] = "Binod                  Tiwari"
dm.close()

from abc import ABCMeta, abstractmethod


class Something(metaclass=ABCMeta):
    def sth(self):
        self.busy()
    @abstractmethod
    def busy(self):
        pass

class Sub(Something):
    def busy(self):
        print("sth is in")
        self.play()

    def play(self):
        print("I'm playing the game now.")
        self.slay()
    def slay(self):
        print("I'm fading away.")


b = Sub()
b.sth()

class u:
    pass
x = u()
x.__dict__["a"] = "b"
print(x.a)

class zero:
    a = 9
    def sth(self):
        return "sth is great"
    def __add__(self, other) -> str:
        self.k = 10
        return "add"
    def __iadd__(self, other):
        self.p=10
        return "iadd"
    def __radd__(self, other):
        return "radd"
    def __or__(self, other):
        return "or"
i = zero()
print(bin(9), i.a, bin(3))
i |= 46
print(i, )          # doesn't work i.sth()

import  sys
class Checker:
    def __init__(self, start, end,b=0):
        print(start, end)
        self.start = start
        self.end = end
        self.b = b
    def __iter__(self):
        print("Hero")
        return self
    def __next__(self ):
        print("hero")
        self.b = self.b + 1
        if self.b > 5:
            sys.exit()  # better raise StopIteration
        else:
            return "man you're persistent"


a = Checker(2, 3)
print(type(a))
for i in a:
    print(i)


class Err(Exception):
    pass
x = None
try:
    x = 1 / 0
except ZeroDivisionError:
    pass
finally:
    print('Cleaning up ...')
    del x
f = Err()
n = super(Err,f).__init__()
print("noningn", n, [1, 2])


import heapq, random

a = [3, 2, 1, 4, 5, 6]
b = []
for i in a:
    print("a-->", a)
    heapq.heappush(b, i)
    print("b-->", b)
print("b-->", b)
heapq.heappop(b)
print("b-->", b)
heapq.heappush(b, 0.9)
print(b)
heapq.heapreplace(b, 9)
print(b)
print(heapq.nlargest(2, a))

from collections import deque

queue = deque(range(1, 11))
print(queue)
queue.pop()
print(queue)
queue.appendleft(11)
print(queue)
queue.pop()
queue.pop()
queue.pop()
queue.pop()
queue.pop()
queue.pop()
print(queue)
queue.reverse()
print(queue)
queue.pop()
print(queue)
help(queue.rotate)
queue.extendleft(["idea","drik"])
print(queue)

import time
a = time.time()
def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False

def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num-1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result

def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length-pos-1)
    for pos in solution:
        print(line(pos))
import random
k=0
for i in list(queens(10)):
    prettyprint(i)
    print("\n\n")
    k += 1
b= time.time()
print(b - a, k)

def load():
    with open(filename.get()) as file:
        contents.delete('1.0', END)
        contents.insert(INSERT, file.read())
def save():
    with open(filename.get(), 'w') as file:
        file.write(contents.get('1.0', END))
top = Tk()
top.title("Simple Editor")
contents = ScrolledText()
contents.pack(side=BOTTOM, expand=True, fill=BOTH)
filename = Entry()
filename.pack(side=LEFT, expand=True, fill=X)
Button(text='Open', command=load).pack(side=RIGHT)
Button(text='Save', command=save).pack(side=RIGHT)
mainloop()

import shelve

a = shelve.open("unknown.txt")
a["b"] = [1, 2, 3, 4, 5, 6, 7]
a["c"] = "98889"
a["b"].append(1)
print(a["b"], a["c"], b := iter(a.keys()), b.__next__())

a.close()
"""
numlist = [i for i in range(26)]
alpha_list = [chr(i) for i in range(97, 123)]
dict = {i+1: alpha_list[i] for i in numlist}
list = [6,0,2,2,1,4,1,4,1,0,7,0,4,0,9,0,8,4,0,9,9,0,7,2]
str=''
for i in list:
	if i !=0:
		str = str + dict[i]
print(str)