#Frequency of characters in a string
string = "automation"
string = input("Enter the input e.g automation")

#  { a :2, u:1, t:2,o:2,m:1, i:1, n:1}

char_count={}

#logic buliding
#i/p-string
#o/p- dict #  { a :2, u:1, t:2,o:2,m:1, i:1, n:1}

for char in string:
    char_count[char]= char_count.get(char,0)+1

print(char_count)
