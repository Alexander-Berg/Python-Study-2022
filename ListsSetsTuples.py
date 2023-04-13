# DRINKING GAME: Take a shot every time I say the word pineapple

#   List  = [] ordered and changeable. Duplicates OK
#   Set   = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER
fruits = ["apple", "orange", "banana", "coconut", "coconut"]
print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("pinneaple" in fruits)
fruits.add("pinneaple")
fruits.remove("apple")
fruits.pop()
print(fruits.count("coconut"))
print(fruits)
for fruit in fruits:
    print(fruit)


