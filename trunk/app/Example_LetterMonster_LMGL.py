
import os, sys
sys.path.insert( 0, os.getcwd() )
from _letter_monster import LetterMonster

print( 'Starting to read LMGL file...\n' )

#

lm = LetterMonster()
lm.DEBUG = True

lm.Load( 'test_lmgl.yaml' )
print( 'LMGL successfully loaded.' )

lm.body['raster1'].data = lm.bp.StrToYamlNdarray('Raster\n0 0 0\ndata', False)
lm.body['raster1'].z=2

lm.body['raster3'].data = lm.bp.StrToYamlNdarray('.\n.', False)
lm.body['raster3'].visible=True

lm.body['vect1'].data = 'NEW DATA'
lm.body['vect1'].origin = (99,10)

print( 'Changed some data...' )

try: os.remove( 'test_lmgl_n.yaml' )
except: pass

lm.Save( 'test_lmgl_n.yaml' )
print( 'New LMGL successfully modified.' )

#

print( 'Finished.\n' )
os.system( 'pause' )

#
