
import os, sys
sys.path.insert( 0, os.getcwd() )
from _letter_monster import LetterMonster

print( 'Starting to read LMGL file...\n' )

#

lm = LetterMonster()
lm.DEBUG = True

lm.Bite( 'test_lmgl.xml' )
print( 'LMGL successfully loaded.' )

lm.body['vect1'].data = 'My NEW data'
lm.body['vect1'].origin = '99,10'
print( 'Changing some data...' )

try: os.remove( 'test_lmgl_s.xml' )
except: pass

lm.Spawn( 'test_lmgl_s.xml' )
print( 'New LMGL successfully modified.' )

#

print( 'Finished.\n' )
os.system( 'pause' )

#
