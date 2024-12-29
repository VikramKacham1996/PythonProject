#Dictionary from  two  lists

keys= ['a','b','c']
values= [1,2,3]
my_dict= dict(zip(keys,values))
print(my_dict)

###
keys= ['emp1','emp2','emp3']
values= [100,200,300]
my_dict= dict(zip(keys,values))
print(my_dict)

###
keys= ("1","2","3")
value=("1","2","3")
my_dict =dict(zip(keys,value))
print(my_dict)

###
keys=("name", "role", "exp")
value=("Vikky", "Python Developer", "6 years")
my_dict=dict(zip(keys, value))
print(my_dict)

#Merge 2 dictionaries


dic1={"1","2"}
dic2={"11","22"}
merge_dic=dic1|dic2
print(merge_dic)

dic1 = {"a":1, "b":2}
dic2 = {"c":3, "d":4}
merge_dic=dic1|dic2
print(merge_dic)
print(merge_dic.get("a"))
print(merge_dic.get("e"))