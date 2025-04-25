#Write a class called Password
# _manager. The class should have a list called old
# _passwords that
# holds all of the user’s past passwords. The last item of the list is the user’s current pass word.
# There should be a method called get_password that returns the current password and a method
# called set_password that sets the user’s password. The set_password method should only
# change the password if the attempted password is different from all the user’s past passwords.
# Finally, create a method called is_correct that receives a string and returns a boolean True or
# False depending on whether the string is equal to the current password or not.

class Passwordmanager:

    def __init__(self,cp):
                self.current_pass = []
                self.current_pass.append(cp)
        
    

    
    def get_password(self):
        return print(self.current_pass[len(self.current_pass)-1])

    
    def set_password(self,user_pass):
        if user_pass in self.current_pass:
                    
                    self.current_pass.append(user_pass)
        else:
             return print('Password can not be change ')
    
    def is_correct(self,attemp_pass):
           return self.current_pass[len(self.current_pass)-1] == attemp_pass 
           
           

u1 = Passwordmanager("HArsh1204")

u1.get_password()
u1.set_password("HArsh04")
print(u1.is_correct("HArsh1204"))

        

