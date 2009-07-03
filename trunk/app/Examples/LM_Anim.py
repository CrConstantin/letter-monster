# -*- coding: latin-1 -*-
'''
Letter-Monster Engine v0.2.9
Copyright © 2009, Cristi Constantin. All rights reserved.
This one is Letter-Monster's FIRST animation ! It requires Pygame.
Enjoy.
The original image is called "Rotating Skeleton" and it's made by Tomi J. Maksa.
Check his profile : http://www.pixeljoint.com/p/22334.htm
'''

import os, sys, thread, time, pygame
sys.path.insert( 0, os.getcwd().replace('Examples','')[:-1] )
from _letter_monster import LetterMonster

lm = LetterMonster()
lm.DEBUG = True
lm.Load( 'LM_Anim.lmgl' )

for x in range(4): # Start a few FlattenLayers threads.
    thread.start_new_thread( lm.FlattenLayers, (True, ), )
    time.sleep(0.1)

pygame.init()
vScreen = pygame.display.set_mode( (330, 580) )
vFont = pygame.font.SysFont('Lucida Console', 8)
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
        vFR = vFont.render(''.join(vLine), True, (200, 233, 255)) # Render font with blue.
        vScreen.blit(vFR, (1,i))
        i += vHeight
    #
    pygame.display.flip()
    #
#
