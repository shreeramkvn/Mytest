x = "There are %d types of people." % 10 # Types of people mentioned here
binary = "binary" # format of binary is 0 and 1
do_not = "don't" # donot is mentioned as don't
y = "Those who knows %s and those who %s." % (binary, do_not) # partitioning who knows binary and who dont
print x # prints the string given for x
print y # prints the string given for y
print "I said: %r." % x #prints x with the given string
print "I also said: %r." % x # prints y with the given string
hilarious = False # explaining binary "0"
evaluation = "Isn't that so funny?! %r" # giving string for the variable
print evaluation % hilarious # printing both declared string
w = "This is the left side  of..." # defining another variable with string
e = "a string width a right side." # defining another variable with string2
print w+e # printing variable and string.
