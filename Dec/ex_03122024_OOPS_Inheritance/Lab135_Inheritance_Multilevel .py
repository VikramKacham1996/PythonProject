#Multilevewl inheritance

#GF ->F ->Son
# grandfather have 2kg gold so grandfather  giving to father and father giving to son

class GrandFather:
    gold = "2kg"

    def bhk1(self):
        print("1BHK")

class Father(GrandFather):
    diamond ="22 karat"

    def BHK2(self):
        print("2BHK")


class Son(Father):
    btc = "1BTC"

    def BHK3(self):
        print("3BHK")

s = Son()
print(s.gold)
print(s.diamond)
print(s.btc)
print(s.BHK2)
print(s.bhk1)
print(s.BHK3)

f = Father()
print(f.gold)
print(f.diamond)
print(f.bhk1)
print(f.BHK2)

g= GrandFather()
print(g.gold)
print(g.bhk1)


# like nested









