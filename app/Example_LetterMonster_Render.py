# -*- coding: latin-1 -*-
'''
Letter-Monster Engine v0.2.9
Copyright © 2009, Cristi Constantin. All rights reserved.
This is a simple example for rendering a LMGL file on the screen, via Pygame.
'''

import os, sys
sys.path.insert( 0, os.getcwd() )
from _letter_monster import LetterMonster

lm = LetterMonster()
lm.DEBUG = True
lm.Number_Of_Threads = 1

lm.Load( 'test_event.lmgl' )
print

lm.Render('pygame', size=(300,200), fontsize=10, txtcolor=(166, 166, 255), bgcolor=(33, 33, 33))

os.system( 'echo Done.&pause' )

#
