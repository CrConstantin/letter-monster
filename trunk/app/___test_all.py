
import os, sys, glob
sys.path.insert( 0, os.getcwd() )

try: from _classes import *
except: print "Error on importing _Classes module!"

try: from _letter_monster import *
except: print "Error on importing LetterMonster module!"

# Test 1.
try: import Example_Backpack_Strip_Center_Border
except: print "Error on importing Example_Backpack_Strip_Center_Border!"

# Test 2.
try: import Example_LetterMonster_Consume
except: print "Error on importing Example_LetterMonster_Consume!"

# Test 3.
try: import Example_LetterMonster_LMGL
except: print "Error on importing Example_LetterMonster_LMGL!"

# Test 4.
try: import Example_LetterMonster_LMGL_Border
except: print "Error on importing Example_LetterMonster_LMGL_Border!"

# Test 5.
try: import Example_LetterMonster_Spawn
except: print "Error on importing Example_LetterMonster_Spawn!"

# Test 6.
try: import Example_LetterMonster_Spit
except: print "Error on importing Example_LetterMonster_Spit!"

pyc = glob.glob( '*.pyc' )
for p in pyc:
    try: os.remove( p )
    except: pass
lmgl = glob.glob( '*.lmgl' )
for l in lmgl:
    try: os.remove( l )
    except: pass
os.system('pause')
