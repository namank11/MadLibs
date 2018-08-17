# mad lib generator
# let the user input parts of speech for use in a madlib
adj1 = str(input('Let\'s mad lib!; give me and adjective and press enter. '))
n1 = str(input('Okay, now a plural noun. '))
n2 = str(input('A singular noun. '))
adj2 = str(input('Another adjective, and brace yourself for hilarity. '))

# title
print('\nDon\'t be caught in a lurch this Valentine\'s Day!\n')

# combine the input words with text
print('roses are ' + adj1 + '.')
print(n1 + ' are blue.')
print(n2 + ' is ' + adj2 + '.')
print('And so are you!')