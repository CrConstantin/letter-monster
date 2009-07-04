# -*- coding: latin-1 -*-
'''
Letter-Monster Engine v0.3
Copyright © 2009, Cristi Constantin. All rights reserved.
This one is Letter-Monster's SECOND animation ! It requires Pygame.
Enjoy.
The original image is called "grinkitty" and it's made by Samantha McGunagle.
Check her profile : http://cryztaldreamz.deviantart.com
'''

import os, sys
sys.path.insert( 0, os.getcwd().replace('Examples','')[:-1] )
from _letter_monster import LetterMonster

lm = LetterMonster()
lm.DEBUG = True
lm.Load( 'LM_Grin_Kitty.lmgl' ) # Change LMGL file here.
lm.Render( 'pygame', size=(330,590) )
