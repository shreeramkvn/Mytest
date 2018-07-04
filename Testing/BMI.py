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
print ("So, you are a %r years old, %r Cms tall, and %r Kgs heavy.\n\n" % (a, h, w))

z = ((703)*(w/(h*h)))

print ("For your age %r, BMI Value is %r kg/m^2." %(a, z))
if z <= 16:
    print("You are Underweight please contact a doctor for your health")
elif z>=16 and z<=17:
	print("You are lesser in health than regular. Please have a good diet to increase your health")
elif z>=17 and z<=19:
	print("You are good in health than regular. Please have a good diet to increase your health")
elif z>=19 and z<=25:
	print("Your health is normal, please maintain the same diet and workout")
elif z>=25 and z<=30:
	print("You are overweighted. Please maintain good diet and correct excercies to have you under normal")
elif z>=30 and z<=35:
	print("You are Obessed. OBESE CLASS I. Please have a good diet to increase your health")
elif z>=35 and z<=40:
	print("You are Obessed. OBESE CLASS II. Please have a good diet to increase your health")
else:
	print("You are Obessed. OBESE CLASS II and have a very bad health habits!!! Please do regular exercises and consult your doctor for a good health!!!")




#print ("What is your gender? (M/F)")
#gender = input()
#if gender=='m' or 'M':
#	print ("Male")
#elif gender=='f' or 'F':
#	print ("Female")
#else:
#	print ("Transgender")


#x=(h/100)
#float(x)
#y=(x*x)
#float(y)
#z=(w/y)
#float(z)
#print ("So, you are a %r of  %r years old, %r Cms tall, and %r Kgs heavy." % (gender, age, height, weight))
