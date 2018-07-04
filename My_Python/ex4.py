# shows total number of cars that are available
cars = 100

space_in_car = 4.0 #Shows the occupancy that a car can do

drivers = 30 #shows the number of drivers available

cars_not_driven = cars - drivers # cars not driven = the cars without drivers

passengers = 150 # Shows the number of passengers that is available

cars_driven = drivers # shows the count of cars that are being driven

carpool_capacity = cars_driven * space_in_car # capacity using which each car can be car-pooled

average_passengers_per_car = passengers / cars_driven # shows the average people that a car can transport

trip_count = passengers / drivers # shows the number of trips that each car has to do if it has to drop all passengers

per_car_transport = passengers / space_in_car # shows the number of trips that one car has to do if it has to drop all passengers.

overall_transport = (passengers / space_in_car)/drivers

overall_trips = cars_driven+(cars_driven*0.25)

print "There are ", cars , " cars available."

print "There are only ", drivers , " drivers available to drive ", cars , " cars."

print "There will be ", cars_not_driven ," cars without drivers to drive them."

print "We will be able to transport ", carpool_capacity ," number of people having", passengers ," as the count of passengers available"

print "On an average, cars would have make around ", trip_count ," trips to drop ", passengers ," passengers today."

print "We have ", passengers ," to carpool today."

print "We may need to occupy ", average_passengers_per_car ," in each car to complete all ", passengers ," passengers using carpool."

print "If we occupy only ", space_in_car ," passengers per car and use only one car, we will be able to complete all", passengers ," in around ", per_car_transport ,"trips."

print "If we occupy only ", space_in_car ," passengers per car and use only one car, we will be able to complete all", passengers ," in around ", per_car_transport ,"trips."

print "If we occupy only ", space_in_car ," passengers per car and use all the cars, we will be able to complete all", passengers ," in around ", overall_transport ,"trips."

print "That is", overall_trips ,"trips with", drivers ,"cars. Which can also be said as", overall_trips- drivers ,"plus", drivers, "trips. So that one car will transport", 0.5*4, "people for one trip."

print "Hey %s there." % "you"
