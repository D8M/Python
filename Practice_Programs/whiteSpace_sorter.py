# Whitespace removal & sorted words

sentence = input("\nEnter some whitespace seperated words please: ")

words = sentence.split(" ")
set_of_words = set(words)

sorted_set_of_words = sorted(set_of_words)

print(" ".join(sorted_set_of_words))
