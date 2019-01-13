
name = ('Zed. A. Shaw')
age = 35
height = 74 #in inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
force = 'Regardless'

print ("Let's talk about  %s." % name)
print ("He's %s inches tall" % height)
print ("He weighs %s pounds" % weight)
print ("Actually he's not too heavily")
print ("Hes got %s eyes and %s hair" % (eyes, hair))
print ("His teeth are usualy %s depending on the coffee" % teeth)

#this is a tricky
print ("If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight))

#extra code for the assignment / example 5
print ("This is testing a new format charater that prints %r" % force)


#height in feet and inches to centemetres calculator - commented out
#print("Input your height: ")
#h_ft = int(input("Feet: "))
#h_inch = int(input("Inches: "))

#h_inch += h_ft * 12
#h_cm = round(h_inch * 2.54, 1)

#print("Your height is : %d cm." % h_cm)

#height in centremetres from feet and inches
print("Input your height: ")
h_cm = float(input("CM: "))

h_inch = h_cm / 2.54
h_ft = h_inch / 12

print("Your height is : %d ft." % h_ft)