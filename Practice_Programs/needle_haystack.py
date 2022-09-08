clean_haystack = ["hay", "hay", "hay", "hay", "hay"]
unclean_haystack = [ "hay", "hay", "hay", "needle", "hay"]

search_for = "needle"

max = len(clean_haystack)
i = 0

while i  < max:
    if search_for == clean_haystack[i]:
        print("The %s is at index %i: "  % (search_for, i ))

        del clean_haystack[i]
        break

    i = i + 1

else:
    print("\The needle was not found :( ")
    
