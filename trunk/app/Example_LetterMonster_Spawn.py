
import os, sys
sys.path.insert( 0, os.getcwd() )
from _letter_monster import LetterMonster

print( 'Starting to read LMGL file...\n' )

#

lm = LetterMonster()
lm.DEBUG = True

lm.Spawn( 'test_lmgl_c.yaml', 'txt' )

#

print( 'Finished.\n' )
os.system( 'pause' )

#
