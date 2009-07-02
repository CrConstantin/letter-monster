# -*- coding: latin-1 -*-
'''
Letter-Monster Engine v0.2.5
Copyright © 2009, Cristi Constantin. All rights reserved.
This module generates a test LMGL file to play with. You can use it for Spawn, Spit or Execute.
'''

import os, sys
sys.path.insert( 0, os.getcwd() )
from _classes import *
from _letter_monster import LetterMonster

lm = LetterMonster()
lm.DEBUG = True

# Background layer is a border with dots inside.
r = Raster( name = 'raster1', visible = True, transparent = u' ', z = 1, offset = (0,0),
        data = lm.VA._Transform('s2a', '#'*30+'\n' + 10*('#'+'.'*28+'#\n') + '#'*30), )
lm.body[ r.name ] = r
del r

# Middle layer is a grid of * (stars).
r = Raster( name = 'raster2', visible = False, transparent = u' ', z = 2, offset = (1,1),
        data = lm.VA._Transform('s2a', ('* '*14+'\n')*10 ), )
lm.body[ r.name ] = r
del r

# This layer move to create an animation.
r = Raster( name = 'raster3', visible = True, transparent = u'', z = 3, offset = (5,5),
        data = lm.VA._Transform('s2a', '.^.\n^|^\n^.^'), )
lm.body[ r.name ] = r
del r

# Event onload.
e = Event(name = 'onload', call_macro = 'onload_macro')
lm.body[ e.name ] = e
del e

# This macro will be called be called imediately after loading the LMGL file.
instruct = [ {
            'f':'new',
            'layer':'vector',
            'name':'vector2',
            'instructions':[{'f':'Border','Input':'raster2','Char':'.'}],
            'z':2,
           }, ]
m = Macro( name = 'onload_macro', instructions=instruct )
lm.body[ m.name ] = m
del m ; del instruct

# Event onrender.
e = Event(name = 'onrender', call_macro = 'onrender_macro')
lm.body[ e.name ] = e
del e

# This macro is called for each render loop.
instruct = [ {
            'f':'change',
            'name':'raster3',
            'offset':('8-self.fps_nr%8', 5),
           }, ]
m = Macro( name = 'onrender_macro', instructions=instruct )
lm.body[ m.name ] = m
del m ; del instruct

#

print( 'Added data...' )
try: os.remove( 'test_event.lmgl' )
except: pass
lm.Save( 'test_event.lmgl', 'y' )
os.system( 'echo Done.&pause' )

#
