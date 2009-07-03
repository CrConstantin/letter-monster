
import os, sys, thread, time, pygame
sys.path.insert( 0, os.getcwd().replace('Examples','')[:-1] )
from _letter_monster import LetterMonster

lm = LetterMonster()
lm.DEBUG = True
lm.Load( 'test_event.lmgl' )

for x in range(lm.Number_Of_Threads): # Start a few FlattenLayers threads.
    thread.start_new_thread( lm.FlattenLayers, (True, ), )
    time.sleep(0.1)

pygame.init()
vScreen = pygame.display.set_mode( (320, 240) )
vFont = pygame.font.SysFont('Lucida Console', 12)
vHeight = vFont.get_height()

#
while 1:
    #
    time.sleep( lm.max_fps ) # Sleep a little...
    #
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.KEYDOWN):
            lm.vCanLoop = False
            print( 'Letter-Monster says: "Key pressed, exiting..."' )
            pygame.quit() ; sys.exit()
    #
    vScreen.fill((0, 0, 0)) # Paint screen with black.
    #
    vFrame = lm.FrameBuffer.get()
    lm.FrameBuffer.task_done()
    i = 1
    #
    for vLine in vFrame:
        vFR = vFont.render(''.join(vLine), True, (0, 255, 255)) # Render font with blue.
        vScreen.blit(vFR, (1,i))
        i += vHeight
    #
    pygame.display.flip()
    #
#
