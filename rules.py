import pygame
import XO

pygame.init()
pygame.display.set_caption('XO')
clock = pygame.time.Clock()
# reasloution
display_surface = pygame.display.set_mode(( 600, 600 ))
# setting
XO.game.GetGame(3,3)
winner = 0
turn = 0
stuts = True
#=========
def display (picture,x,y):
    display_surface.blit(pygame.image.load(f'pictures/{picture}.png'), (x,y))
def text(text):
    font = pygame.font.Font("freesansbold.ttf", 30)
    text = font.render(text, True, [255, 255, 255], [0, 0, 0])
    textRect = text.get_rect()
    textRect.center = (300, 300)
    display_surface.blit(text, textRect)
def cordnation():
    cor = []
    click_pos = pygame.mouse.get_pos()
    cor.extend([int(click_pos[0]/200),int(click_pos[1]/200)])
    return cor
def run(): #every farme : 60 FPS
    #display
    clock.tick(60)
    global stuts, turn, winner
    display("bourd",0,0)
    for i in range (0,len(XO.Gamebourd)):
        for j in range (0,len(XO.Gamebourd[i])):
            if XO.Gamebourd[i][j] != str(0):
                display(XO.Gamebourd[i][j],(i*200)+10,(j*200)+10)
    if stuts == False:
        display("over",0,0)
        text(winner)
    for event in pygame.event.get() :
        if event.type == pygame.MOUSEBUTTONDOWN:
            postion = cordnation()
            if stuts == False:
                stuts = True
                XO.game.GetGame(3,3)
                break
            if stuts == True:
                if XO.Gamebourd[postion[0]][postion[1]] == str(0):
                    if turn%2 == 0:
                        XO.game.input(postion[0],postion[1],"x")
                        turn = turn + 1
                    else:
                        XO.game.input(postion[0],postion[1],"o")
                        turn = turn +1
                    if XO.game.CheckLine("H")[0] == True or XO.game.CheckLine("V")[0] == True or XO.game.CheckCross()[0] == True or XO.game.CheckDraw()[0] ==  True:
                        stuts = False
                        if XO.game.CheckLine("H")[1] == 360 or XO.game.CheckLine("V")[1] == 360 or XO.game.CheckCross()[1] == 360:
                            winner = "X WON"
                        if XO.game.CheckLine("H")[1] == 333 or XO.game.CheckLine("V")[1] == 333 or XO.game.CheckCross()[1] == 333:
                            winner = "O WON"
                        if XO.game.CheckDraw()[1] == 1:
                            winner = "DRAW"
        if event.type == pygame.QUIT :
            pygame.quit()
    try:
        pygame.display.update()
    except:
        quit()
