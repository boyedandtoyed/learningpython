class Restaurant:
    """
    All I know about restaurant
    """
    def __init__(self, name, location, time):
        self.name = name
        self.location = location
        self.time = time
        self.number_served = 0
    def restaurant_info(self):
         print ("The restaurant,", self.name.title(), "is situated in", self.location.title(),"avenue.")
    def restaurant_openess(self):
        # whether restaurant is open
        if self.time >= 8 and self.time <= 20:
            return ("Restaurant is open. You're welcome.")
        else:
            a = ("Sorry, restaurant is currently close.")
            b = (" Better come tommorow between 8 in the morning to 8 in evening.")
            c = a + b
            return c
    def _numbers_served(self,no_of_serves):
        self.number_served = no_of_serves
        return ("There were in total "+ str(self.number_served)+ " serves.")
    def _additional_served(self,extra_serves):
        self.number_served += extra_serves
        return ("There is now in total " + str(self.number_served)+ " serves.")





class User:
    def __init__(self,first_name,last_name, education_level, experties_area):
        self.first_name = first_name
        self.last_name = last_name
        self.education_level= education_level
        self.experties_area=experties_area
        self.login_attempts=0

    def greetings(self):
        print("Hello" , self.first_name,end="! ")
    def description_of_user(self):
        print("Here's everything we know about you: ")
        print("Your full name is ", self.first_name.title()," ", self.last_name.title(),".",sep="")
        print("You are expert in the field of ",self.experties_area.title(),".",sep="")
        print("You've studied upto ", self.education_level.title(),".",sep="")
    def increament_login_attempts(self):
        self.login_attempts +=1
        return self.login_attempts
    def reset_login_attempts(self):
        self.login_attempts=0
        return self.login_attempts


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
