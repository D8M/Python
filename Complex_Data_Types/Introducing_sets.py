# Sets = collection of unique elements, no duplicates, no order & doesnt support indexing or when printed unlike lists
# Elements are not KV pairs, just elements. Sets are classes. Can be mixed.
# Lists cannot be part of a set
# Elements in a set are immutable

set_names = {"David", "James"}
print("\n", set_names)

set_names.add("Caesar")
print("\n", set_names)

# set_names.discard('') -> does nothing if element does not exist
# set_names.remove('') -> can throw error if element does not exist

# PERFORMING SET OPS

new_set_names = {"Peter", "James", "John"}
# Merges but lops off the extra James!
merged_names = set_names.union(new_set_names)
print("\n", merged_names)

# set1.intersection(set2) #-> Finds common numbers to all sets

# set1.difference.(set2) #-> All elements left after removing common or shared elements
#diff_set = student1.difference(student2)

# set1.intersection_update(set2) -> Invoking intersection_update command on set1
# Performs intersection check and updates found elements to set1 -> changes set1, set2 unchanged

# {1,2,3}.isdisjoint({4,5,6}) # Whether sets contain elements in common or not = true or flase, false if common exists 

# {10,20}.issubset({10,20,30}) # = True
# {10,20}.issuperset({10,20,30}) # = False

# L1 = ["bacon", "eggs"]
# L2 = ["toast", "jam"]
# brunch = L1
# L1.append("juice")
# brunch.extend(L2)
# print(brunch)
a = 8
b =3
print( 'Addition:\t' , a , '+', b , '=' , a + b )  

print( 'Floor Division:\t' , a , '÷', b , '=' , a // b )
print( 'Modulus:\t' , a , '%', b , '=' , a % b )         
2
 
print( 'Exponent:\t ' , a , '² = ' , a ** b , sep = '' ) 