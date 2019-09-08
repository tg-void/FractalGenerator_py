# FractalGenerator_py
A fractal is "a curve or geometric figure, each part of which has the same statistical character as the whole". Searching for them on Google yields some very pretty results.
This is an ongoing project.

Notes I took in the code for ways to improve:
#1 understand the formula for x2 and y2 and pygame.draw.line() and pygame.display.flip()
#2 allow for choice btwn tree fractal and sunflower fractal (and others)
#3 separate fractal choices into entirely isolated functions
#4 allow for range of depths to be entered along with appropriate window size and x1 & y1 values to match
#5 allow user input via GUI
#6 loop so that consistently move between menu screen (holding available choices and exit) and pictures
#7 allow pictures to be saved as .png or .jpeg if desired
#8 have exit key or button to go back to menu from picture
#9 for x2 and y2 formula, multiply by log(depth) to prevent size of each drawn line from getting too large

What I have completed:
#1 created colorChoice() function to randomize color; used in pygame.draw.line() to create a randomly colored tree everytime the program is run
