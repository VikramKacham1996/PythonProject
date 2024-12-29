cities =( "karimnagar", "delhi", "bangalore", "mumbai", "chennai", "Vijayawada" )

print("karimnagar" in cities)

print("patna" in cities)


t= (12,34,56)
# t.append (12) # AttributeError: 'tuple' object has no attribute 'append'
my_list = list(t)
my_list.append(1)
t = tuple(my_list)
print(t)

env_api__urls = ("https://api.github.com/users/vikky/repos", "https://api.github.com/users/patelkumar/repos", "https://api.github.com/users/kumar/repos")
print(env_api__urls)