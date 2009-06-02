# -*- coding: latin-1 -*-
'''
Letter-Monster Engine v0.2.
Copyright © 2009, Cristi Constantin. All rights reserved.
Spawn is Export function.
'''

import os, sys
sys.path.insert( 0, os.getcwd() )
from _letter_monster import LetterMonster

lm = LetterMonster()
lm.DEBUG = True

print( 'Spawning...\n' )
lm.Spawn( lmgl='test_cons.lmgl', out='txt' )

os.system( 'echo Done. Sleeping 5...&sleep 5' )

#
