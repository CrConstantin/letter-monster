# -*- coding: utf-8 -*-
'''
Letter-Monster Engine.
Copyright © 2009, Cristi Constantin. All rights reserved.
#
This module calls all examples, to test them and show the order in which they can be tested.
If you want to see more, you must edit some of the files.
For example, to see how "lmgl_bord.lmgl" looks like,
    you must first run "Example_LetterMonster_LMGL_Border.py", to generate the file "lmgl_bord.lmgl",
    then edit "Example_LetterMonster_Spit.py" and change the string in Load function
    from 'test.lmgl' to 'lmgl_bord.lmgl'. Now run the Spit Example.
'''

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
try: import Example_LetterMonster_Render
except: print "Error on importing Example_LetterMonster_Render!"

# Test 7.
try: import Example_LetterMonster_Spit
except: print "Error on importing Example_LetterMonster_Spit!"

# Del pyc and lmgl.
pyc = glob.glob( '*.pyc' )
for p in pyc:
    try: os.remove( p )
    except: pass
lmgl = glob.glob( '*.lmgl' )
for l in lmgl:
    try: os.remove( l )
    except: pass
try: os.remove( 'out.txt' )
except: pass
os.system('echo Finished. Sleeping 10...&sleep 10')
