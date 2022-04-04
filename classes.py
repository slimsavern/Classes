class User():
    first_name = ""
    middle_name= ""
    last_name = ""
    email_address = ""
    phone_number = ""
    allergies = ""
    user_type = ""
    is_active = False

    def get_full_name(self):
        return "{} {} {}".format(self.first_name, self.middle_name ,self.last_name)

class MealItem():
    
    id=""
    name = ""
    description = ""
    serving_size = ""
    portion_control = ""
    allergens = ""


class Order():
    meals = ""





class Review():
    feedback = ""

user = User();
user.first_name = "John"
user.middle_name = "Doe"
user.last_name = "Smith"
user.email_address = "Johndoe@gmail.com"
user.phone_number = "0246330667"
user.allergies = "Peanuts"
user.user_type = "Customer"
user.is_active = True

print("Hello I am {}".format(user.get_full_name()))

