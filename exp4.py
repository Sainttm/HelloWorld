#!!Hover over the variable to confirm how Python has set it - int, string, float, boolian

#create a variable called 'cars' and assign it a int value of '100'
cars = 100
#create a variable called 'space_in_a_car' and assign it the FP value of '4.0' 
#note: FP = Floating point aka decimal place and following digits
space_in_a_car = 4.0
#create a variable called 'drivers' and assign it the int value of '30'
drivers = 30
#create a variable called 'passengers' and assign it the int value of '90'
passengers = 90
#create a variable called 'cars_not_driven' then have the number of ..
#..cars available minus the number of drivers to give the remaing number of cars not drivern
cars_not_drivern = cars - drivers
#create a variable called 'cars_drivern' then have it equalling / setting to the number of.. 
#..drivers
cars_driven = drivers
#create a variable called 'carpool_capacity' then have the number of cars_driven * the ..
#..space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
#Final variable to delcare 'average_passengers_per_car' then have the number of passengers ..
#.. divide by the number of cars drivern
average_passengers_per_car = passengers / cars_driven

#Set up the print strings with the above variables mixed where applicable
print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_drivern, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car")