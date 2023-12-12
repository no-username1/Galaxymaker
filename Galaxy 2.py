from turtle import *
print("Turtle has been imported")
from random import *
print("Random has been imported")


def moveToRandomLocation():
    penup()
    print("penup")
    setpos(randint(-400, 400), randint(-400, 400))
    print("Move turtle to random location")
    pendown()
    print("penup")

# a function for drawing a star of a particular size
def drawStar(starSize, starColour):
    color(starColour)
    pendown()
    begin_fill()
    for side in range(5):
        left(144)
        forward(starSize)
    end_fill()
    print("Fill Ended")
    penup()
    print("Penup")


def drawGalaxy(numberOfStars):
    print("Defining DrawGalaxy")
    starColours = ["#058396","#0275A6","#827E01"]
    moveToRandomLocation()
    # draw lots of small coloured stars
    for star in range(numberOfStars):
        penup()
        print("Penup")
        left(randint(-180, 180) )
        forward(randint(5, 20) )
        print("Drawing small colured stars")
        pendown()
        # draw a small star in a random colour
        drawStar( 2, choice(starColours) )
        print("Drawing small star in a random colour")

# a function for drawing a joined constellation of stars
def drawConstellation(numberOfStars):
    moveToRandomLocation()
    print("Draw all stars expect last one")
    # joined by lines, like this: *--*--*--
    for star in range(numberOfStars-1):
        drawStar(randint(7, 15) , "white")
        pendown()
        left(randint(-90, 90) )
        forward(randint(30, 70) )
    # now draw the last star
    drawStar(randint(7, 15) , "White")

speed(11)

bgcolor("MidnightBlue")
print("Changing Background to Dark Blue")
# draw 30 white stars (random sizes/locations)
for star in range(30):
    print("Draw 30 white stars in random sizes/locations")
    moveToRandomLocation()
    drawStar(randint(5, 25) , "White")

# draw 3 small galaxies of 40 stars
for galaxy in range(3):
    print("Make galaxy")
    drawGalaxy(40)
    print("Drawing 40 stars")

# draw 2 constellations, each with a random number of stars
for constellation in range(2):
    print("Draw 2 constellations")
    drawConstellation(randint(4, 7))

hideturtle()
print("Hiding Turtle")
print("Complete")
done()