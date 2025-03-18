from Dec.ex_03122024_OOPS_Inheritance.Lab133_Inheritance_single import father_obj


class Parent:
    gold = "2kg"

    def __init(self):
        Print("DC-Parent")

    def BHK2(self):
        print("2BHK")
class Child(Parent):

    def __init(self):
        Print("DC-Parent")

    diamond ="Diamond"
    def BHK3(self):
        print("3BHK")

child_object = Child()
print(child_object.gold)
child_object.BHK2()

father_object_ref = Parent()
father_object_ref.BHK2()
#father_object_ref.BHK3()


#single inheritance son getting everything from father


