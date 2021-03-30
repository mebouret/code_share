def buildRainbow(colorList):
    numberOfColors = len(colorList)
    rainbowScene.add(Rect(0, 0, 400, 400, fill='skyBlue'))
    for colIncr in range(numberOfColors):
        radius = 200 - (colIncr * 25)
        rainbowScene.add(Circle(200, 200, radius, fill=colorList[colIncr]))
    skyCircRadius = 200 - (numberOfColors * 25)
    rainbowScene.add(Circle(200, 200, skyCircRadius, fill='skyBlue'))
    rainbowScene.add(Rect(0, 200, 400, 400, fill='springGreen'))



colors = ['red', 'orange', 'yellow', 'green','blue', 'indigo', 'purple']
rainbowScene = Group()

buildRainbow(colors)

# Challenge: use the append or pop method for lists to add or remove one or more colors.

# Challenge: change each color in the list to its pastel
# or lighter color version using indexing.

# Challenge: change the rainbow's theme to another color scheme.

# Challenge: what is the radius of the sky circle at the center?

# Challenge: balance the rainbow's bands with the addition or subtraction
# of colors.

# Challenge: use the choice method for lists to randomly generate your rainbow's color order.

# Challenge: animate the rainbow with the step function and with different color schemes
