
import os, sys
sys.path.insert( 0, os.getcwd() )
from _classes import *
from _letter_monster import LetterMonster

lm = LetterMonster()
lm.DEBUG = True

r = Raster()
lm.body['raster1'] = r
lm.body['raster1'].name = 'raster1'
lm.body['raster1'].visible = True
lm.body['raster1'].data = lm.bp._Transform('s2a', '#'*30+'\n' + 10*('#'+' '*28+'#\n') + '#'*30 )
lm.body['raster1'].z=1
del r

r = Raster()
lm.body['raster2'] = r
lm.body['raster2'].name = 'raster2'
lm.body['raster2'].visible = True
lm.body['raster2'].data = lm.bp._Transform('s2a', '\n\n  I am Johny.')
lm.body['raster2'].z=2
del r

r = Raster()
lm.body['raster3'] = r
lm.body['raster3'].name = 'raster3'
lm.body['raster3'].visible = True
lm.body['raster3'].data = lm.bp._Transform('s2a', '\n\n\n  Johny Mnemonic.')
lm.body['raster3'].z=3
del r

print( 'Added data...' )
try: os.remove( 'test_b.lmgl' )
except: pass
lm.Save( 'test_b.lmgl' )

print( 'Finished.\n' )
os.system( 'pause' )

#
