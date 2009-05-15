
import os, sys
sys.path.insert( 0, os.getcwd() )
from _letter_monster import LetterMonster

#

lm = LetterMonster()
lm.DEBUG = True

lm.Load( 'test_lmgl.yaml' )
print

lm.Spit('WIN CMD')
print

#

os.system( 'pause' )

#
