
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
lm.body['raster1'].data = lm.bp._Transform('s2a', 'R a s t e r 1\nsome data')
lm.body['raster1'].z=2
del r

r = Raster()
lm.body['raster2'] = r
lm.body['raster2'].name = 'raster2'
lm.body['raster2'].visible = True
lm.body['raster2'].data = lm.bp._Transform('s2a', '00000\n11111\n22222\n33333\n44444')
lm.body['raster2'].z=1
del r

r = Raster()
lm.body['raster3'] = r
lm.body['raster3'].name = 'raster3'
lm.body['raster3'].visible = True
lm.body['raster3'].data = lm.bp._Transform('s2a', '    .\n    .\nlast line of raster3')
lm.body['raster3'].z=3
del r

v = Vector()
lm.body['vect1'] = v
lm.body['vect1'].name = 'vect1'
lm.body['vect1'].instructions = [
    {'f':'Rotate90Right','vInput':'raster1'},
    {'f':'FlipH','vInput':'vect1'},
    {'f':'StripRightSpace','vInput':'vect1'},
    {'f':'Center','vInput':'vect1'} ]
lm.body['vect1'].origin = (99,10)
del v

e = Event()
lm.body['event1'] = e
lm.body['event1'].name = 'event1'
lm.body['event1'].affect = 'aff'
del e

m = Macro()
lm.body['macro1'] = m
lm.body['macro1'].name = 'macro1'
lm.body['macro1'].instructions = 'instr'
del m

print( 'Added data...' )
try: os.remove( 'test.lmgl' )
except: pass
lm.Save( 'test.lmgl' )

print( 'Finished.\n' )
os.system( 'pause' )

#
