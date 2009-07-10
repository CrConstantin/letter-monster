# -*- coding: latin-1 -*-
'''
Letter-Monster Engine v0.3
Copyright © 2009, Cristi Constantin. All rights reserved.
This one is Letter-Monster's FIRST animation ! It requires Pygame.
Enjoy.
The original image is called "Rotating Skeleton" and it's made by Tomi J. Maksa.
Check his profile : http://www.pixeljoint.com/p/22334.htm
'''

import os, sys
sys.path.insert( 0, os.getcwd().replace('Animations','')[:-1] )
from _letter_monster import LetterMonster

lm = LetterMonster()
lm.DEBUG = True
lm.Number_Of_Threads = 1
lm.Load( 'LM_Rotating_Skeleton.lmgl' ) # Change LMGL file here.
lm.Render( 'pygame', size=(323,577), txtcolor=(255, 255, 255), bgcolor=(33, 33, 66) )
