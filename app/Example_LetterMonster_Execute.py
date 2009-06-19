# -*- coding: latin-1 -*-
'''
Letter-Monster Engine v0.2.2.
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
lm._Execute( 'vect1', 'autorun' )

print 'Executing macro instructions...\n'
lm._Execute( 'macro1', 'autorun' )

print lm.body

os.system( 'echo Done.&pause' )

#
