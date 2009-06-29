# -*- coding: latin-1 -*-
'''
Letter-Monster Engine v0.2.5
Copyright © 2009, Cristi Constantin. All rights reserved.
This module demonstrates transforming an Image into a LMGL file.
This file can be later rendered (check Spit example) or exported (check Spawn example).
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

lm.Consume( image='Logo.jpg', x=0, y=0, pattern='default', filter='' )

try: os.remove( 'test_cons.lmgl' )
except: pass
lm.Save( 'test_cons.lmgl', 'p:bz2' )

print 'Body 1: ', lm.body, '\n'
print 'Data is len:', len(lm.body['raster1'].data)
print 'Data[0] is len:', len(lm.body['raster1'].data[0]),'\n'

print( "Please, use Lucida Console Bold, size 4 for viewing." )

os.system( 'echo Done.&pause' )

#
