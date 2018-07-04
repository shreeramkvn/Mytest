myname = "Venkatesh"
myage = 29 # originally
myheight = 6.2 # is not fake
myweight = 86 # in kilos
myeyes = "brown" # eye colour
myteeth = "ivory" # Teeth colour
myhair = "black" # Hair colour

print "lets speak about %s." %myname
print "%s's height is %d foot." %(myname, myheight)
print "%s's weight is %d Kilos." %(myname, myweight)
print "Actually this is a bit heavy." 
print "%s's got %s eyes and %s hair." %(myname, myeyes, myhair)
print "%s's teeth is usually %s in colour." %(myname, myteeth)

# most funny part is here

print "If i add %d, %d, and %d, I get %d." % (myage, myheight, myweight, myage + myheight + myweight    )
