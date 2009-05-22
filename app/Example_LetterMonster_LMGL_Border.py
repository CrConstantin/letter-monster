# -*- coding: utf-8 -*-
'''
Letter-Monster Engine.
Copyright © 2009, Cristi Constantin. All rights reserved.
This module generates a LMGL file to play with. You can use it for Spawn or Spit.
'''

import os, sys
sys.path.insert( 0, os.getcwd() )
from _classes import *
from _letter_monster import LetterMonster

lm = LetterMonster()
lm.DEBUG = True

r = Raster(
    name = 'raster1',
    visible = True,
    data = lm.bp._Transform('s2a', '#'*40+'\n' + 10*('#'+' '*38+'#\n') + '#'*40 ),
    z=1, )
lm.body[ r.name ] = r
del r

r = Raster(
    name = 'raster2',
    visible = True,
    data = lm.bp._Transform('s2a', '\n\n  I am Johny.'),
    z=2, )
lm.body[ r.name ] = r
del r

r = Raster(
    name = 'raster3',
    visible = True,
    data = lm.bp._Transform('s2a', '\n\n\n  Johny Bravo.\n\n\n\n\n\n  Am i cool or what ;>'),
    z=3, )
lm.body[ r.name ] = r
del r

print( 'Added data...' )
try: os.remove( 'test_bord.lmgl' )
except: pass
lm.Save( 'test_bord.lmgl' )

print( 'Finished.\n' )
os.system( 'pause' )

#
