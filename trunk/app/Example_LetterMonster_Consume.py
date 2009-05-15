
import os, sys
sys.path.insert( 0, os.getcwd() )
from _letter_monster import LetterMonster

#

lm = LetterMonster()
lm.DEBUG = True

lm.Consume( image='../Wallpaper1.jpg', x=0, y=0, pattern='default' )

try: os.remove( 'test_lmgl_cons.yaml' )
except: pass
lm.Save( 'test_lmgl_cons.yaml' )

print 'Body 1: ', lm.body, '\n'
print 'Data is type:', type(lm.body['raster1'].data)
print 'Inside Data, is type:', type(lm.body['raster1'].data[0])
print 'Data is len:', len(lm.body['raster1'].data)
print 'Data 0-10:', lm.body['raster1'].data[0][0:10]

print( "Please, use Lucida Console Bold, size 4 for viewing." )

#

print( 'Finished.\n' )
os.system( 'pause' )

#
