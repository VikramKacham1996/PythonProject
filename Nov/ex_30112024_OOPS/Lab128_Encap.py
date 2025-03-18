class VWOLoginPage:
    def __init__(self, email_arg, password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "vikram@gmail.com" and self.password == "Pass123":
            print("Allowed, Login success")
        else:
            print("Login Failed")

# Take user input for email and password
# email = input("Enter the email: \n")
# password = input("Enter the password: \n")

# Create an object of VWOLoginPage and call login_confirm
# vwo_obj = VWOLoginPage(email, password)
# vwo_obj.login_confirm()

vikram = VWOLoginPage("vikram@gmail.com" , "Pass123")
vikram.login_confirm()
