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

r = Raster( name = 'raster1', visible = True, transparent = u' ', z = 3, offset = (0,0),
    data = lm.VA._Transform('s2a', 'R a s t e r 1\nsome data'), )
lm.body[ r.name ] = r
del r

r = Raster( name = 'raster2', visible = True, transparent = u' ', z = 2, offset = (0,0),
    data = lm.VA._Transform('s2a', '00 00\n11 11\n22 22\n33 33\n44 44'), )
lm.body[ r.name ] = r
del r

r = Raster( name = 'raster3', visible = True, transparent = u' .', z = 4, offset = (0,0),
    data = lm.VA._Transform('s2a', '. .\n. .\nlast line of raster3'), )
lm.body[ r.name ] = r
del r

instruct = [
    {'f':'Rotate90Right','Input':'raster2'},
    {'f':'Rotate90Left','Input':'vect1'},
    {'f':'StripRightSpace','Input':'vect1'},
    {'f':'StripLeftSpace','Input':'vect1'},
    {'f':'Border','Input':'vect1','Char':'='}
    ]
v = Vector( name = 'vect1', instructions=instruct, offset = (0,0), z = 2, )
lm.body[ v.name ] = v
del v ; del instruct

e = Event(name = 'event1', affects = 'aff')
lm.body[ e.name ] = e
del e

instruct = [
    {'f':'new', 'layer':'event', 'name':'event2', 'affects':'', 'affect_macro':''},
    {'f':'ren', 'name':'event2', 'newname':'event222'},
    {'f':'change', 'name':'event222', 'affects':'new aff'},
    {'f':'del', 'name':'event222'},
    ]
m = Macro( name = 'macro1', instructions=instruct )
lm.body[ m.name ] = m
del m ; del instruct

#

print( 'Added data...' )
try: os.remove( 'test.lmgl' )
except: pass
lm.Save( 'test.lmgl', 'y' )
os.system( 'echo Done.&pause' )

#
