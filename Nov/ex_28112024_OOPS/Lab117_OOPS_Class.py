class person:
    # attributes -what yoy have?

    id = None
    name = None
    age = None
    email = None
    height = None
    geneder = None
    phone_no = None
    address = None

    #behaviour -What you can do?

    def talk(self, name):#NRNG # self -this, self will be first argument in every
        print("i  can talk")

    def sleep(self, name): # Arg with return
        print("I am a method")
    def sleep2(self):
        print("iam  amethod!!")

    def walk(self):
        print("i am walking")
    def walk_return(self):
        return " iam  walking"
#create an object of the class
#objectRef.name =  ClassName() -> Object
geeta = person()
geeta.name = " geetha sharma"
geeta.gender= "female"