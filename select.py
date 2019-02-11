python_words={'list': 'A collection of values that are not connected, but have an order.',
              'dictionary':'A collection of key-value pairs.',
              'function':'A named set of instructions that defines a set of actions in Python'}

print("The following python words have been defined:")
for word in python_words:
  print("- %s" % word)

requested_word=input("\nWhat word would you like to learn about?")
print("\n%s: %s" %(requested_word,python_words[requested_word]))
