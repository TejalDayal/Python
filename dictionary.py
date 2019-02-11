python_words={'list': 'A collection of values that are not connected, but have an order.',
              'dictionary':'A collection of key-value pairs.',
              'function':'A named set of instructions that defines a set of actions in Python'}

print('dictionary:' + python_words['dictionary'])

#Clarify one of the meanings.
python_words['dictionary']='A collection of key-value pairs. \
                            Each key can be used to access its corresponding value.'

print('\ndictionary:' + python_words['dictionary'])
