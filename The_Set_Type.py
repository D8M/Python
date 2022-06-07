# The Set type allows for creating immutable elements
empty_set = set()  # set constructor

alpha = set(('a', 'b', 'c', 'd', 'e'))  # Set of Tuple
print("Alpha Set: ", alpha)  # Creates unordered list

duplicate_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
                  'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

beta = set(duplicate_list)
print("Beta or no duplicates in List: ", beta)

gamma = alpha.union(beta)
print("Gamma set unioned with Beta set: ", gamma)
# or gamma = alpha (vertical pipe key?) beta

delta = alpha.intersection(beta)
print("Delta intersection Beta is: ", delta)

epsilon = alpha.difference(beta)
print("Alpha set difference Beta set: ", epsilon)

eta = alpha.symmetric_difference(beta)
print("Eta is the Symmetric Defference: ", eta)

# To see if any set has elements in common with another set use .isdisjoint
print("Do These sets (alpha, delta) have anything in common?", alpha.isdisjoint(beta)
      )
print("Do These sets (epsilon, gamma) have anything in common?", epsilon.isdisjoint(gamma)
      )
