# -*- coding: utf-8 -*-
'''
Letter-Monster Engine.
Copyright © 2009, Cristi Constantin. All rights reserved.
This is a simple example for rendering a LMGL file on the screen, via WIN CMD.
'''

import os, sys
sys.path.insert( 0, os.getcwd() )
from _letter_monster import LetterMonster

lm = LetterMonster()
lm.DEBUG = True

lm.Load( 'test.lmgl' )
print

lm.Spit('WIN CMD', autoclear=True)
print

os.system( 'pause' )

#
