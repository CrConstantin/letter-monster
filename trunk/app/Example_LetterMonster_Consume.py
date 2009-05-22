# -*- coding: utf-8 -*-
'''
Letter-Monster Engine.
Copyright © 2009, Cristi Constantin. All rights reserved.
This module demonstrates transforming an Image into a LMGL file.
This file can be later rendered (check Spit Example) or exported (check Spawn example).
The transformation can be direct from Image to ASCII, by calling Consume, then Spawn as txt.
You can choose another pattern for transformation.
Filters can be applied on the image, separated by "|" (vertical line).
For the list of valid patterns and filters check "LetterMonster" class, function "__init__".
'''

import os, sys
sys.path.insert( 0, os.getcwd() )
from _letter_monster import LetterMonster

lm = LetterMonster()
lm.DEBUG = True

lm.Consume( image='../Wind_by_pincel3d.jpg', x=0, y=0, pattern='default', filter='' )

try: os.remove( 'test_cons.lmgl' )
except: pass
lm.Save( 'test_cons.lmgl' )

print 'Body 1: ', lm.body, '\n'
print 'Data is type:', type(lm.body['raster1'].data)
print 'Inside Data, is type:', type(lm.body['raster1'].data[0]),'\n'
print 'Data is len:', len(lm.body['raster1'].data)
print 'Data[0] is len:', len(lm.body['raster1'].data[0]),'\n'
print 'Data 0-10:', lm.body['raster1'].data[0][0:10]

print( "Please, use Lucida Console Bold, size 4 for viewing." )

print( 'Finished.\n' )
os.system( 'pause' )

#
