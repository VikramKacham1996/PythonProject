class XYZ:
    def f1(self):
        try:
            a = int(input("enter a number\n"))
        except Exception as e:
            print("enter int only value of a")
        else:
            print(a)
        finally:
            print("Finally: anyhow i will be printed")
x_obj_ref =XYZ()
x_obj_ref.f1()