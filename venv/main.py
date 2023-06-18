import turtle
import csv
import math

# Screen Set Up

sc = turtle.Screen()
tr = turtle.Turtle()
sc.title("Count Parking Slots")
image = "park-parking-lot-plan.gif"
sc.setup(650,397)
sc.addshape(image)
sc.bgpic("park-parking-lot-plan.gif")
tr.speed("fastest")


with open("CPS_Middle_Parking_Slot_Point.csv", "r") as mid_slot_csv:
    reader = csv.reader(mid_slot_csv)
    for row in reader:
        print(row)
        tr.penup()
        tr.goto(float(row[0]),float(row[1]))
        tr.dot(10,"green")


def read_specific_row(user_input):
    with open("CPS_Middle_Parking_Slot_Point.csv", "r") as mid_slot_csv:
        reader = csv.reader(mid_slot_csv)
        for index, row in enumerate(reader):
            if index + 1 == user_input:
                return row

    return None


def claim_parking_slot(coor_x,coor_y):
    tr.penup()
    tr.goto(coor_x,coor_y)
    tr.dot(10,"red")

while True:
    user_input = sc.numinput("Poker", "Your stakes:", 1000, minval=10, maxval=10000)
    coor = read_specific_row(user_input)
    coor_x = float(coor[0])
    coor_y = float(coor[1])
    claim_parking_slot(coor_x,coor_y)
sc.mainloop()