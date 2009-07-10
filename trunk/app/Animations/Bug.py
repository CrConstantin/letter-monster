# -*- coding: latin-1 -*-
'''
Letter-Monster Engine v0.3
Copyright © 2009, Cristi Constantin. All rights reserved.
This one is Letter-Monster's THIRD animation ! It requires Pygame.
Enjoy.
The original image is called "bug.gif". I don't know who is the author, i'm sorry.
'''

import os, sys
sys.path.insert( 0, os.getcwd().replace('Animations','')[:-1] )
from _letter_monster import LetterMonster

lm = LetterMonster()
lm.DEBUG = True
lm.Number_Of_Threads = 1
lm.Load( 'Bug.lmgl' ) # Change LMGL file here.
lm.Render( 'pygame', size=(250,510), txtcolor=(0, 0, 0), bgcolor=(100, 155, 133) )
