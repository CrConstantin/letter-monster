
import os, sys
sys.path.insert( 0, os.getcwd() )
from _letter_monster import LetterMonster

#

lm = LetterMonster()
lm.DEBUG = True

print( 'Spawning...\n' )
lm.Spawn( 'test_lmgl_cons.yaml', 'txt' )

#

print( 'Finished.\n' )
os.system( 'pause' )

#
