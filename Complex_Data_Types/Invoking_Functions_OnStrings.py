from posixpath import split


place = "Ballynacloghy Maree Oranmore"

print(place.startswith("B"))
print(place.startswith("b"))
print(place.endswith("b"))
print(place.count("b"))
print(place.count("B"))

lower_place = place.lower()
print(lower_place)

upper_place = place.upper()
print(upper_place)
print(lower_place == upper_place)
print(place.find("B"))
print(place.count(" "))
split_place = place.split(" ")
print(split_place)
print(len(split_place))
join_char = ","
print(join_char.join(split_place))

