
import os, sys
sys.path.insert( 0, os.getcwd() )
from _letter_monster import LetterMonster

#

lm = LetterMonster()
lm.DEBUG = True

lm.Load( 'test_lmgl.yaml' )
print 'Executing vector instructions...\n'
print 'Instructions are', lm.body['vect1'].instructions
print 'Instructions are type:', type(lm.body['vect1'].instructions)
print 'Inside instructions, there is type:', type(lm.body['vect1'].instructions[0]), '\n'

lm._execute( 'vect1' )
print

#

print( 'Finished.\n' )
os.system( 'pause' )

#
