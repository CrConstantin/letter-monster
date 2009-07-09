# -*- coding: latin-1 -*-
'''
Letter-Monster Engine v0.2.9
Copyright © 2009, Cristi Constantin. All rights reserved.
This module transforms a GIF animated pic into a LMGL file.
You can use the LMGL file for ASCII animations.
'''

import os, sys, shutil
import Image
sys.path.insert( 0, os.getcwd() )
from _letter_monster import LetterMonster

lm = LetterMonster()
lm.DEBUG = True

# This is the name of your GIF animated picture.
vImageName = 'bug.gif'

# Create a directory to store the resulted images.
try: os.mkdir( os.getcwd() + '/' + 'Gif_2_LMGL' )
except: pass

vFrames = 0 # Save frame number.
im = Image.open( vImageName )
for frame in range(999):
    try:
        im.seek(frame)
        vFrames = frame+1
    except: break
print 'Image has %i frames.' % vFrames

for frame in range(vFrames):
    #
    im = Image.open( vImageName ) # The image must be re-opened every loop.
    for frm in range(frame+1):    # Try to move to next frame.
        im.seek(frm)
    #
    # Now save the frame image on HDD, as PNG.
    vResultedImage = os.getcwd() + '/' + 'Gif_2_LMGL/img' + str(frame) + '.PNG'
    im.save( vResultedImage, **im.info )
    lm.Consume( image=vResultedImage, x=0, y=0, pattern='default' )
    #

try: shutil.rmtree( os.getcwd() + '/' + 'Gif_2_LMGL' ) # Delete temporary directory.
except: pass
try: os.remove( 'Gif_2_LMGL.lmgl' ) # Delete old LMGL.
except: pass
lm.Save( 'Gif_2_LMGL.lmgl', 'y' ) # Save new LMGL.

os.system( 'echo Done.&pause' )
