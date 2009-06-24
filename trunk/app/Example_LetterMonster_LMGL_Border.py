# -*- coding: latin-1 -*-
'''
Letter-Monster Engine v0.2.2.
Copyright © 2009, Cristi Constantin. All rights reserved.
This module generates a test LMGL file to play with. You can use it for Spawn or Spit.
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
    transparent = u'',
    data = lm.VA._Transform('s2a', '#'*30+'\n' + 10*('#'+'.'*28+'#\n') + '#'*30 ),
    z=1, )
lm.body[ r.name ] = r
del r

r = Raster(
    name = 'raster2',
    visible = True,
    transparent = u'-', # Transparent character : -. It will be ignored at rendering.
    offset = (2,2),
    data = lm.VA._Transform('s2a', 'I-am-Johny.'),
    z=2, )
lm.body[ r.name ] = r
del r

r = Raster(
    name = 'raster3',
    visible = True,
    transparent = u' ',
    offset = (3,2),
    data = lm.VA._Transform('s2a', 'Johny Bravo.\n\n\n\n\n\nAm i cool or what ;>'),
    z=3, )
lm.body[ r.name ] = r
del r

print( 'Added data...' )
try: os.remove( 'test_bord.lmgl' )
except: pass
lm.Save( 'test_bord.lmgl', mode='y:bz2' )

os.system( 'echo Done.&pause' )

#
