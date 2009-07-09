# -*- coding: latin-1 -*-
'''
Letter-Monster Engine v0.2.9
Copyright © 2009, Cristi Constantin. All rights reserved.
Spawn is in fact an Export function.
Can export as 'txt', 'csv', 'html', 'bmp', 'gif', 'jpg', 'png', 'pdf', 'ps'.
'''

import os, sys
sys.path.insert( 0, os.getcwd() )
from _letter_monster import LetterMonster

lm = LetterMonster()
lm.DEBUG = True

print( 'Loading...\n' )
lm.Load( 'test_cons.lmgl' )

print( 'Spawning...\n' )
#lm.Export( out='txt', filename='Export' )
lm.Spawn( out='txt', filename='Export' ) # Spawn == Export.


os.system( 'echo Done.&pause' )

#
