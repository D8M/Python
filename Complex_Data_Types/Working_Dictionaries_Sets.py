# Dicts in Py are mutable
empty_dict = {

}

# Dict is defined as a mapping of key value pairs
what_they_own = {
    # Keys------Values
    "James": "JCB 3CX",
    "Conor": "Abrams M1 Tank",
    "Kate": "Tesla Model S",
    "Emma": "F14 Tomcat"

}
# Shows what value asscioated with the key
print("\n", what_they_own["Conor"])
# Shows list of all keys in that Dict
print("\n", what_they_own.keys())
# Shows list of all values in that Dict
print("\n", what_they_own.values())

# Inserting new KV pair to dict
what_they_own["Mum & Dad"] = "6 Berth Camper"
what_they_own["James"] = "Mercedes S Class"  # Updating a KV pair
print("\n", what_they_own)
# del what_they_own["Emma"] -- deleting a passed in key of Emma

int_dict = {1: 45, 2: 99, 3: 0}
print("\n", int_dict[2])
print("\n", int_dict.get(1))

# Keys should be unique
# Mixed dicts are ok - have booleans, floats, strings etc in one dict
