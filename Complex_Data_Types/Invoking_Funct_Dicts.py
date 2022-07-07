
what_they_own = {
    # Keys------Values
    "James": "JCB 3CX",
    "Conor": "Abrams M1 Tank",
    "Kate": "Tesla Model S",
    "Emma": "F14 Tomcat"
}

print("\n", len(what_they_own))  # Len -> Gives number of KV pairs

print("\n", sorted(what_they_own))  # Sorts Keys in lexographical order...?

print("\n", sorted(what_they_own, reverse=True))  # Sorts Keys in reverse

# To sort values pass in to sorted function
# print("\n",sorted(what_they_own.values())) #-> returns error in E College course..?

what_they_own.items()
print("\n", what_they_own)  # Returns as a set for me , not tuple

copy_of_what_they_own = what_they_own.copy()
print("\n", copy_of_what_they_own)

# Pops off a key value pair -> does not effect original dict
copy_of_what_they_own.pop('James')
print("\n", copy_of_what_they_own)

# copy_of_what_they_own.popitem() # -> Randomly pops off a KV pair

# How to update a dict with new data
dict_age = {'David': 50, 'James': 11, 'Kate': 12}
new_dict_age = {'David': 51, 'James': 11, 'Kate': 13}

dict_age.update(new_dict_age)
print("\nDict showing updated ages: ", dict_age)

# To Clear dict
# copy_of_what_they_own.clear() # or del to delete dict completely
