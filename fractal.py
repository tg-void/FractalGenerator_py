import pygame, math, random
 
pygame.init() #initialize all imported pygame modules
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface() #screen defined "globablly" so drawTree() can access it

def colorChoice(): #produces RGB value for varition in colored parts
    return random.randint(100, 255)

def drawTree(x1, y1, angle, depth):
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        pygame.draw.line(screen, (colorChoice(),colorChoice(),colorChoice()), (x1, y1), (x2, y2), 2)
        drawTree(x2, y2, angle - 20, depth - 1)
        drawTree(x2, y2, angle + 20, depth - 1)
 
def input(event):
    if event.type == pygame.QUIT:
        exit(0)

init_x1 = 300
init_y1 = 550
initAngle = -90
drawTree(init_x1, init_y1, initAngle, 9)
pygame.display.flip()
while True:
    input(pygame.event.wait()) #pauses screen so it can be viewed

#a lot of room for improvement
#1 understand the formula for x2 and y2 and pygame.draw.line() and pygame.display.flip()
#2 allow for choice btwn tree fractal and sunflower fractal (and others)
#3 separate fractal choices into entirely isolated functions
#4 allow for range of depths to be entered along with appropriate window size and x1 & y1 values to match
#5 allow user input via GUI
#6 loop so that consistently move between menu screen (holding available choices and exit) and pictures
#7 allow pictures to be saved as .png or .jpeg if desired
#8 have exit key or button to go back to menu from picture
#9 for x2 and y2 formula, multiply by log(depth) to prevent size of each drawn line from getting too large
