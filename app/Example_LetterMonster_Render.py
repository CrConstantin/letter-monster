# -*- coding: latin-1 -*-
'''
Letter-Monster Engine v0.2.8
Copyright © 2009, Cristi Constantin. All rights reserved.
This is a simple example for rendering a LMGL file on the screen, via Pygame.
'''

import os, sys
sys.path.insert( 0, os.getcwd() )
from _letter_monster import LetterMonster

lm = LetterMonster()
lm.DEBUG = True

lm.Load( 'test_event.lmgl' )
print

lm.Render('pygame')

os.system( 'echo Done.&pause' )

#
