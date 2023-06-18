import turtle
import csv

# Screen Set Up

sc = turtle.Screen()
tr = turtle.Turtle()
sc.title("Count Parking Slots")
image = "park-parking-lot-plan.gif"
sc.setup(650,397)
sc.addshape(image)
tr.shape(image)

sc.mainloop()