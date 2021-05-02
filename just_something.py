def names(first_name,last_name,middle_name=""):
    if middle_name:
        formatted_name=(first_name +" "+middle_name + " "+ last_name).title()
    else:
        formatted_name=(first_name+" "+last_name).title()
    return formatted_name
import  unittest
class Name_Test(unittest.TestCase):
    def test_my_function(self):
        """Does my name binod tiwari work?"""
        formatted_name=names("binod","tiwari")
        self.assertEqual(formatted_name,"Binod Tiwari")
    def test_my_second_condition(self):
        """Does my name binod prasad tiwari work?"""
        formatted_name=names("binod","tiwari","prasad")
        self.assertEqual(formatted_name,"Binod Prasad Tiwari")
