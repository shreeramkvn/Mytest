import datetime 
now = datetime.datetime.now()
days = "Mon Tue Wed Thu Fri Sat Sun"
month = "\n Jan \n Feb \n Mar \n Apr \n May \n Jun \n Jul \n Aug \n Sep \n Oct \n Nov \n Dec"
print "Here are the Days : ",days
print "Below are the Months : ",month
print """
Writing text into 3 double quotes.
There is something going on here.
We can type data as much as we are able to type in here.
Even 4 - 5 lines may be 10 to 20 if needed.
"""
print "Current time with date is as below, this includes milliseconds of the current time too : \n",now
print "Today is : ", now.day
