# -*- coding: latin-1 -*-
'''
Letter-Monster Engine v0.2.
Copyright © 2009, Cristi Constantin. All rights reserved.
This module demonstrates executing instructions stored inside a vector layer, in one LMGL file.
'''

import os, sys
sys.path.insert( 0, os.getcwd() )
from _letter_monster import LetterMonster

lm = LetterMonster()
lm.DEBUG = True

lm.Load( 'test.lmgl' )

print 'Executing vector instructions...\n'
print 'Instructions are', lm.body['vect1'].instructions
print 'Instructions are type:', type(lm.body['vect1'].instructions)
print 'Inside instructions, there is type:', type(lm.body['vect1'].instructions[0]), '\n'

lm._execute( 'vect1' )

os.system( 'echo Done. Sleeping 5...&sleep 5' )

#
