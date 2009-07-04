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
vImageName = 'grinkitty.gif'

# Create a directory to store the resulted images.
try: os.mkdir( os.getcwd() + '/' + 'Gif_2_LMGL' )
except: pass

im = Image.open( vImageName )
for frame in range(999):
    # Try to move to next frame.
    try: im.seek(frame)
    except: break
    #
    new = im.convert( 'RGBA' )
    # Now save the frame image on HDD, as BMP.
    vResultedImage = os.getcwd() + '/' + 'Gif_2_LMGL/img' + str(frame) + '.png'
    new.save( vResultedImage )
    lm.Consume( image=vResultedImage, x=65, y=0, pattern='default' )

try: shutil.rmtree( os.getcwd() + '/' + 'Gif_2_LMGL' )
except: pass
try: os.remove( 'Gif_2_LMGL.lmgl' )
except: pass
lm.Save( 'Gif_2_LMGL.lmgl', 'y' )

print( 'Done!' )