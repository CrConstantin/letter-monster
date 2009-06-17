# -*- coding: latin-1 -*-
'''
    Letter-Monster Engine v0.2.2 \n\
    Copyright © 2009, Cristi Constantin. All rights reserved.\n\
    This module contains Backpack class, with all helper functions and all layer types : Raster, Vector, Event and Macro.\n\
'''

import numpy as np

class Raster:
    '''Raster layer class.\n'''
    #
    def __init__(self, name='', data=np.array([[]],'U'), transparent=u'', offset=(0,0), visible=True, lock=False, z=1):
        self.name = name
        self.data = data
        self.transparent = transparent
        self.offset = offset
        self.visible = visible
        self.lock = lock
        self.z = z
    #
    def __str__(self):
        '''This func is used to identify the type of layer when more layers are stored inside LetterMonster body dictionary.\n'''
        return 'raster'
    #
#

class Vector:
    '''Vector layer class.\n'''
    #
    def __init__(self, name='', data=np.array([[]],'U'), transparent=u'', instructions={}, offset=(0,0), visible=True, lock=False, z=1):
        self.name = name
        self.data = data
        self.transparent = transparent
        self.instructions = instructions
        self.offset = offset
        self.visible = visible
        self.lock = lock
        self.z = z
    #
    def __str__(self):
        '''This func is used to identify the type of layer when more layers are stored inside LetterMonster body dictionary.\n'''
        return 'vector'
    #
#

class Event:
    '''Event layer class.\n'''
    #
    def __init__(self, name='', affects='', affect_macro=''):
        self.name = name
        self.affects = affects
        self.affect_macro = affect_macro
        self.z = -99 # This should be read-only.
    #
    def __str__(self):
        '''This func is used to identify the type of layer when more layers are stored inside LetterMonster body dictionary.\n'''
        return 'event'
    #
#

class Macro:
    '''Macro layer class.\n'''
    #
    def __init__(self, name='', instructions={}):
        self.name = name
        self.instructions = instructions
        self.z = -99 # This should be read-only.
    #
    def __str__(self):
        '''This func is used to identify the type of layer when more layers are stored inside LetterMonster body dictionary.\n'''
        return 'macro'
    #
#

class Backpack:
    '''
This is Backpack class. It contains helper functions. It uses no arguments for initialization.\n\
All functions in Backpack take a Rectangular Unicode Array as input.\n\
'''
    #
    def __init__(self):
        '''Initializes the engine. vContent will always contain last-transformed-data.\n'''
        self.vContent = None
    #
    def __str__(self):
        '''String representation of this abstract class. It's just a fun function to have.\n'''
        return 'I am the Evil Backpack. Baaah!'
    #
    def __test_input(self, INPUT):
        '''
Private validation function. Tests if Input is a 2D Numpy Array.\n\
All helper functions call this before transforming data. If Input is not valid, respective helper function must exit.\n\
'''
        try:
            if str(type(INPUT))=="<type 'numpy.ndarray'>" and str(type(INPUT[0]))=="<type 'numpy.ndarray'>" and len(INPUT.shape)==2:
                return True
            else:
                return False
        except:
            return False
    #
    def _Transform( self, Type, Input ):
        '''
Transforms the input into a Rectangular Unicode Array.\n\
This is the only function that doesn't take a Rectangular Unicode Array as input.\n\
'''
        #
        if Type=='s2a':    # Input is a string containing newline.
            vLines = Input.split('\n')
        elif Type=='ls2a': # Input is a list containing strings split by newline.
            vLines = Input
        else:
            print( 'Backpack yells: "`%s` is an invalid type! Exiting function!"' % Type ) ; return
        #
        vMax = max(len(line) for line in vLines) # Get max lines length.
        vCont = np.zeros((len(vLines),vMax),dtype='U') # Define empty array.
        for i,line in enumerate(vLines):               # Fill array.
            vCont[i,:len(line)] = [j for j in line]
        #
        return vCont
        #
    #
    def Rotate90Right( self, Input, Compress=True ):
        #
        if not self.__test_input(Input): print( 'Backpack yells: "Input is not a rectangular numpy array! Exiting function."' ) ; return
        #
        self.vContent = Input[::-1,:].T # Rotate right.
        #
        print( 'Backpack says: "Done rotating 90 degrees right."' )
        return self.vContent
        #
    #
    def Rotate90Left( self, Input, Compress=True ):
        #
        if not self.__test_input(Input): print( 'Backpack yells: "Input is not a rectangular numpy array! Exiting function."' ) ; return
        #
        self.vContent = Input[:,::-1].T # Rotate left.
        #
        print( 'Backpack says: "Done rotating 90 degrees left."' )
        return self.vContent
        #
    #
    def FlipH( self, Input ):
        #
        if not self.__test_input(Input): print( 'Backpack yells: "Input is not a rectangular numpy array! Exiting function."' ) ; return
        #
        self.vContent = Input[:,::-1] # Reverse elements for every line.
        #
        print( 'Backpack says: "Done reversing content for each line."' )
        return self.vContent
        #
    #
    def FlipV( self, Input ):
        #
        if not self.__test_input(Input): print( 'Backpack yells: "Input is not a rectangular numpy array! Exiting function."' ) ; return
        #
        self.vContent = Input[::-1] # Reverse order of lines, first line becomes last.
        #
        print( 'Backpack says: "Done reversing order of lines."' )
        return self.vContent
        #
    #
    def Reverse( self, Input ):
        #
        if not self.__test_input(Input): print( 'Backpack yells: "Input is not a rectangular numpy array! Exiting function."' ) ; return
        #
        self.vContent = Input[::-1,::-1] # Completely reverse content.
        #
        print( 'Backpack says: "Done reversing content."' )
        return self.vContent
        #
    #
    def StripRightSpace( self, Input ):
        #
        if not self.__test_input(Input): print( 'Backpack yells: "Input is not a rectangular numpy array! Exiting function."' ) ; return
        #
        self.vContent = [ ''.join(i) for i in Input ]
        for x in range( len(self.vContent) ):
            self.vContent[x] = self.vContent[x].rstrip() # Remove extra spaces from the end of the lines.
        self.vContent = self._Transform( 'ls2a', self.vContent )
        #
        print( 'Backpack says: "Done striping right spaces for each line."' )
        return self.vContent
        #
    #
    def StripLeftSpace( self, Input ):
        #
        if not self.__test_input(Input): print( 'Backpack yells: "Input is not a rectangular numpy array! Exiting function."' ) ; return
        #
        self.vContent = [ ''.join(i) for i in Input ]
        for x in range( len(self.vContent) ):
            self.vContent[x] = self.vContent[x].lstrip() # Remove extra spaces from the start of the lines.
        self.vContent = self._Transform( 'ls2a', self.vContent )
        #
        print( 'Backpack says: "Done striping left spaces for each line."' )
        return self.vContent
        #
    #
    def AlignRight( self, Input, Char=u' ' ):
        #
        if not self.__test_input(Input): print( 'Backpack yells: "Input is not a rectangular numpy array! Exiting function."' ) ; return
        #
        self.vContent = [ ''.join(i) for i in Input ]
        vMaxLen = 0
        #
        for vElem in self.vContent:
            if len(vElem) > vMaxLen: # Save lines max length.
                vMaxLen = len(vElem)
        for x in range( len(self.vContent) ):
            self.vContent[x] = self.vContent[x].ljust( vMaxLen, Char ) # Adds extra characters.
        self.vContent = self._Transform( 'ls2a', self.vContent )
        #
        print( 'Backpack says: "Done aligning lines to right."' )
        return self.vContent
        #
    #
    def AlignLeft( self, Input, Char=u' ' ):
        #
        if not self.__test_input(Input): print( 'Backpack yells: "Input is not a rectangular numpy array! Exiting function."' ) ; return
        #
        self.vContent = [ ''.join(i) for i in Input ]
        vMaxLen = 0
        #
        for vElem in self.vContent:
            if len(vElem) > vMaxLen: # Save lines max length.
                vMaxLen = len(vElem)
        for x in range( len(self.vContent) ):
            self.vContent[x] = self.vContent[x].rjust( vMaxLen, Char ) # Adds extra characters.
        self.vContent = self._Transform( 'ls2a', self.vContent )
        #
        print( 'Backpack says: "Done aligning lines to left."' )
        return self.vContent
        #
    #
    def Center( self, Input, Char=u' ' ):
        #
        if not self.__test_input(Input): print( 'Backpack yells: "Input is not a rectangular numpy array! Exiting function."' ) ; return
        #
        self.vContent = [ ''.join(i) for i in Input ]
        vMaxLen = 0
        #
        for vElem in self.vContent:
            if len(vElem) > vMaxLen: # Save lines max length.
                vMaxLen = len(vElem)
        for x in range( len(self.vContent) ):
            self.vContent[x] = self.vContent[x].center( vMaxLen, Char ) # Adds extra characters.
        self.vContent = self._Transform( 'ls2a', self.vContent )
        #
        print( 'Backpack says: "Text centered."' )
        return self.vContent
        #
    #
    def Crop( self, Input, x1, y1, x2, y2 ):
        '''Crop a Rectangular Numpy Array. x1, x2, y1, y2 are zero based indexes.'''
        #
        if not self.__test_input(Input): print( 'Backpack yells: "Input is not a rectangular numpy array! Exiting function."' ) ; return
        #
        self.vContent = Input[x1:x2,y1:y2]
        #
        print( 'Backpack says: "Done cropping text."' )
        return self.vContent
        #
    #
    def Border( self, Input, Char=u' ', Thick=1 ):
        #
        if not self.__test_input(Input): print( 'Backpack yells: "Input is not a rectangular numpy array! Exiting function."' ) ; return
        #
        X = Input.shape[0]
        Y = Input.shape[1]
        vShape = X+Thick*2, Y+Thick*2 # Save new shape.
        vArr = np.empty(vShape, 'U')
        vArr.fill(Char)
        vArr[Thick:X+Thick,Thick:Y+Thick] = Input[:] # Insert Input inside new array.
        #
        self.vContent = vArr
        #
        print( 'Backpack says: "Done adding full border."' )
        return self.vContent
        #
    #
    def RightBorder( self, Input, Char=u' ', Thick=1 ):
        #
        if not self.__test_input(Input): print( 'Backpack yells: "Input is not a rectangular numpy array! Exiting function."' ) ; return
        #
        X = Input.shape[0]
        Y = Input.shape[1]
        vShape = X, Y+Thick # Save new shape.
        vArr = np.empty(vShape, 'U')
        vArr.fill(Char)
        vArr[0:X,0:Y] = Input[:] # Insert Input inside new array.
        #
        self.vContent = vArr
        #
        print( 'Backpack says: "Done adding right border."' )
        return self.vContent
        #
    #
    def LeftBorder( self, Input, Char=u' ', Thick=1 ):
        #
        if not self.__test_input(Input): print( 'Backpack yells: "Input is not a rectangular numpy array! Exiting function."' ) ; return
        #
        X = Input.shape[0]
        Y = Input.shape[1]
        vShape = X, Y+Thick # Save new shape.
        vArr = np.empty(vShape, 'U')
        vArr.fill(Char)
        vArr[0:X,Thick:Y+Thick] = Input[:] # Insert Input inside new array.
        #
        self.vContent = vArr
        #
        print( 'Backpack says: "Done adding left border."' )
        return self.vContent
        #
    #

#
