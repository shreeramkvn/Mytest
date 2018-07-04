#! /usr/bin/env python3.5
"""
This is a funny bmi calculator having math functions

Usage:

	python3 ex11.py

"""
print ("\n\n~~~~FUNNY BMI CALCULATOR~~~~\n\n\n")
print ("How old are you?")
a = input()
float(a)
print ("What is your height? (in CMS)")
h = input()
float(h)
print ("What is your weight? (in KGS)")
w = input()
float(w)
#print ("What is your gender? (M/F)")
#gender = input()
#if gender=='m' or 'M':
#	print ("Male")
#elif gender=='f' or 'F':
#	print ("Female")
#else:
#	print ("Transgender")

print ("So, you are a %r years old, %r Cms tall, and %r Kgs heavy.\n\n" % (a, h, w))
#print ("So, you are a %r of  %r years old, %r Cms tall, and %r Kgs heavy." % (gender, age, height, weight))
x=(h/100)
#float(x)
y=(x*x)
#float(y)
z=(w/y)
#float(z)
print ("Your BMI Value is %r kg/m^2." %(z))
if z>=19 and z<=25:
	print("You have a good health!!!")
else:
	print("You have a bad health!!! Please consult your doctor immediately!!!")

