# A very old joke...
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)

# print the joke
print(x)
print(y)

# print again the joke
print("I said: %r." %x)
print("I also said: %s." %y)

# is it funny?
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print(joke_evaluation % hilarious)
