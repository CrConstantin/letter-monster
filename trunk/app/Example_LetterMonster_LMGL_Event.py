# -*- coding: latin-1 -*-
'''
Letter-Monster Engine v0.2.9
Copyright © 2009, Cristi Constantin. All rights reserved.
This module generates a test LMGL file to play with. It can be used for Events, or Render.
'''

import os, sys
sys.path.insert( 0, os.getcwd() )
from _classes import *
from _letter_monster import LetterMonster

lm = LetterMonster()
lm.DEBUG = True

# Create a background layer : a border with dots inside
r = Raster( name = 'raster1', visible = True, transparent = u' ', z = 1, offset = (0,0),
        data = lm.VA._Transform('s2a', '#'*30+'\n' + 10*('#'+'.'*28+'#\n') + '#'*30), )
lm.body[ r.name ] = r
del r

# Create middle layer : a grid with '*' (stars)
r = Raster( name = 'raster2', visible = False, transparent = u' ', z = 2, offset = (1,1),
        data = lm.VA._Transform('s2a', ('* '*14+'\n')*10 ), )
lm.body[ r.name ] = r
del r

# A little object to move around. Transparent char : '.'
r = Raster( name = 'raster3', visible = True, transparent = u'.', z = 3, offset = (5,5),
        data = lm.VA._Transform('s2a', '..^..\n-^|^-\n.^.^.'), )
lm.body[ r.name ] = r
del r

#
# Set event onrender.
e = Event(name = 'onrender', call_macro = 'onrender_macro')
lm.body[ e.name ] = e
del e
#
# This macro is called each render loop.
instruct = [ {
            'f':'change',
            'name':'"raster3"',
            'offset':'8-self.fps_nr%8,5', # Move up, from 1 to 8.
            },{
            'f':'change',
            'name':'"raster2"',
            'visible':'not bool(self.fps_nr%8)', # Visible only when frame number is % 8.
            }, ]
m = Macro( name = 'onrender_macro', instructions=instruct )
lm.body[ m.name ] = m
del m ; del instruct

# Save everything on HDD.
print( 'Added data...' )
try: os.remove( 'test_event.lmgl' )
except: pass
lm.Save( 'test_event.lmgl', 'y' )
os.system( 'echo Done.&pause' )

#
