# -*- coding: utf-8 -*-
'''
Letter-Monster Engine.
Copyright © 2009, Cristi Constantin. All rights reserved.
This module generates a LMGL file to play with. You can use it for Spawn, Spit or Execute.
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
    data = lm.bp._Transform('s2a', 'R a s t e r 1\nsome data'),
    z = 2, )
lm.body[ r.name ] = r
del r

r = Raster(
    name = 'raster2',
    visible = True,
    data = lm.bp._Transform('s2a', '00000\n11111\n22222\n33333\n44444'),
    z = 1, )
lm.body[ r.name ] = r
del r

r = Raster(
    name = 'raster3',
    visible = True,
    data = lm.bp._Transform('s2a', '    .\n    .\nlast line of raster3'),
    z = 3, )
lm.body[ r.name ] = r
del r

instruct = [
    {'f':'Rotate90Right','Input':'raster1'},
    {'f':'Rotate90Left','Input':'vect1'},
    {'f':'StripRightSpace','Input':'vect1'},
    {'f':'StripLeftSpace','Input':'vect1'},
    {'f':'Border','Input':'vect1'} ]
v = Vector(name = 'vect1', instructions=instruct, position = (99,10))
lm.body[ v.name ] = v
del v

e = Event(name = 'event1', affects = 'aff')
lm.body[ e.name ] = e
del e

m = Macro(name = 'macro1', )
lm.body[ m.name ] = m
del m

print( 'Added data...' )
try: os.remove( 'test.lmgl' )
except: pass
lm.Save( 'test.lmgl' )

os.system( 'echo Done. Sleeping 5...&sleep 5' )

#
