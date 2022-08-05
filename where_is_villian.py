places = ["Ireland","Botswana","Niger","Paraguay","America","Russia","Norway"]

villain_at = "Mali"

for place in places:
    if place == villain_at:
        print("The Police of ",villain_at," have arrested the villian!")
        break
else:
    print("The villain got away again...")
    
