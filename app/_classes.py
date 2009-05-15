#  Letter Monster  #
#        v1        #
#  Helper Classes  #

import numpy as np

class Raster:
    "Raster objects class"
    #
    def __init__(self):
        self.name = ''
        self.data = []
        self.origin = (0,0)
        self.visible = False
        self.lock = False
        self.z = 0
    #
    def __str__(self):
        return 'raster'
    #
#

class Vector:
    "Vector objects class"
    #
    def __init__(self):
        self.name = ''
        self.instructions = []
        self.data = []
        self.origin = (0,0)
        self.visible = False
        self.lock = False
        self.z = 0
    #
    def __str__(self):
        return 'vector'
    #
#

class Event:
    "Event objects class"
    #
    def __init__(self):
        self.name = ''
        self.affect = ''
        self.affect_macro = ''
        self.z = -1
    #
    def __str__(self):
        return 'event'
    #
#

class Macro:
    "Macro objects class"
    #
    def __init__(self):
        self.name = ''
        self.instructions = []
        self.z = -1
    #
    def __str__(self):
        return 'macro'
    #
#

class Backpack:
    '''This is helper functions class.\n\
It uses no arguments for initialization.\n\
All functions in Backpack take vInput as input. vInput MUST be a lis of Unicode Ndarrays.'''
    #
    def __init__(self):
        self.vContent = None
    #
    def __str__(self):
        '''String representation of this abstract class.'''
        return 'I am the Evil Backpack. Baaah!'
    #
    def __test_input(self, INPUT):
        '''Tests of vInput is a valid list of numpy ndarrays.'''
        if str(type(INPUT))=="<type 'list'>" and str(type(INPUT[0]))=="<type 'numpy.ndarray'>":
            return True
        else: return False
    #
    def StrToYamlNdarray( self, vString, Transform=True ):
        '''Transforms the input string into a YAML dump, or into a Ndarray.\n\
This is the only function that doesn't take a list of Unicode Ndarrays as input.'''
        #
        from bz2 import compress
        from yaml import dump, add_representer
        from _letter_monster import ndarray_repr
        add_representer(np.ndarray, ndarray_repr)
        #
        vCont = [ np.array([j for j in i],'U') for i in vString.split('\n') ]
        #
        print( "Done transforming String to YAML !ndarray." )
        if Transform:
            return dump(data=vCont, width=99, indent=4, canonical=False, default_flow_style=False)
        else:
            return vCont
        #
    #
    def Rotate90Right( self, vInput, Compress=True ):
        #
        if not self.__test_input(vInput): print( 'vInput is not a list of numpy ndarrays! Exiting function.' ) ; return
        #
        self.vContent = [ ''.join(i) for i in vInput ]
        self.vContent.reverse()
        vMaxLen = 0
        #
        for vElem in self.vContent:
            if len(vElem) > vMaxLen: # Save lines max length.
                vMaxLen = len(vElem)
        for x in range( len(self.vContent) ): # Add extra spaces to equalize.
            self.vContent[x] = self.vContent[x].rstrip().ljust(vMaxLen)
        #
        vRevCont = map( lambda *row: [elem for elem in row], *self.vContent ) # Rotate the square.
        #
        del self.vContent
        self.vContent = [ ''.join(i) for i in vRevCont ] # Join the sub-lists.
        if Compress:
            for x in range( len(self.vContent) ): # Remove extra spaces from the end of the lines.
                self.vContent[x] = self.vContent[x].rstrip()
        #
        self.vContent = [ np.array([i for i in j],'U') for j in self.vContent ]
        print( "Done rotating 90 degrees right." )
        return self.vContent
        #
    #
    def Rotate90Left( self, vInput, Compress=True ):
        #
        if not self.__test_input(vInput): print( 'vInput is not a list of numpy ndarrays! Exiting function.' ) ; return
        self.vContent = [ ''.join(i) for i in vInput ]
        vMaxLen = 0
        #
        for vElem in self.vContent:
            if len(vElem) > vMaxLen: # Save lines max length.
                vMaxLen = len(vElem)
        for x in range( len(self.vContent) ): # Add extra spaces to equalize.
            self.vContent[x] = self.vContent[x].rstrip().ljust(vMaxLen)
        #
        vRevCont = map( lambda *row: [elem for elem in row], *self.vContent ) # Rotate the square.
        #
        del self.vContent
        self.vContent = [ ''.join(i) for i in vRevCont ] # Join the sub-lists.
        if Compress:
            for x in range( len(self.vContent) ): # Remove extra spaces from the end of the lines.
                self.vContent[x] = self.vContent[x].rstrip()
        #
        self.vContent.reverse()
        self.vContent = [ np.array([i for i in j],'U') for j in self.vContent ]
        print( "Done rotating 90 degrees left." )
        return self.vContent
        #
    #
    def FlipH( self, vInput ):
        #
        if not self.__test_input(vInput): print( 'vInput is not a list of numpy ndarrays! Exiting function.' ) ; return
        #
        vRevCont = []
        for vLine in vInput:
            vRevCont.append( vLine[::-1] ) # Reverse content for each line.
        self.vContent = vRevCont
        #
        print( "Done reversing content for each line." )
        return self.vContent
        #
    #
    def FlipV( self, vInput ):
        #
        if not self.__test_input(vInput): print( 'vInput is not a list of numpy ndarrays! Exiting function.' ) ; return
        #
        vInput.reverse() # Reverse all lines.
        self.vContent = vInput # First line becomes last line.
        #
        print( "Done reversing order of lines." )
        return self.vContent
        #
    #
    def Reverse( self, vInput ):
        #
        if not self.__test_input(vInput): print( 'vInput is not a list of numpy ndarrays! Exiting function.' ) ; return
        #
        vInput.reverse() # Reverse all lines.
        vRevCont = []
        for vLine in vInput:
            vRevCont.append( vLine[::-1] ) # Reverse content for each line.
        self.vContent = vRevCont
        #
        print( "Done reversing content." )
        return self.vContent
        #
    #
    def StripRightSpace( self, vInput ):
        #
        if not self.__test_input(vInput): print( 'vInput is not a list of numpy ndarrays! Exiting function.' ) ; return
        #
        self.vContent = [ ''.join(i) for i in vInput ]
        for x in range( len(self.vContent) ):
            self.vContent[x] = self.vContent[x].rstrip() # Remove extra spaces from the end of the lines.
        self.vContent = [ np.array([i for i in j],'U') for j in self.vContent ]
        #
        print( "Done striping right spaces for each line." )
        return self.vContent
        #
    #
    def StripLeftSpace( self, vInput ):
        #
        if not self.__test_input(vInput): print( 'vInput is not a list of numpy ndarrays! Exiting function.' ) ; return
        #
        self.vContent = [ ''.join(i) for i in vInput ]
        for x in range( len(self.vContent) ):
            self.vContent[x] = self.vContent[x].lstrip() # Remove extra spaces from the start of the lines.
        self.vContent = [ np.array([i for i in j],'U') for j in self.vContent ]
        #
        print( "Done striping left spaces for each line." )
        return self.vContent
        #
    #
    def AlignRight( self, vInput, Char=' ' ):
        #
        if not self.__test_input(vInput): print( 'vInput is not a list of numpy ndarrays! Exiting function.' ) ; return
        #
        self.vContent = [ ''.join(i) for i in vInput ]
        vMaxLen = 0
        #
        for vElem in self.vContent:
            if len(vElem) > vMaxLen: # Save lines max length.
                vMaxLen = len(vElem)
        for x in range( len(self.vContent) ):
            self.vContent[x] = self.vContent[x].ljust( vMaxLen, Char ) # Adds extra characters.
        self.vContent = [ np.array([i for i in j],'U') for j in self.vContent ]
        #
        print( "Done aligning lines to right." )
        return self.vContent
        #
    #
    def AlignLeft( self, vInput, Char=' ' ):
        #
        if not self.__test_input(vInput): print( 'vInput is not a list of numpy ndarrays! Exiting function.' ) ; return
        #
        self.vContent = [ ''.join(i) for i in vInput ]
        vMaxLen = 0
        #
        for vElem in self.vContent:
            if len(vElem) > vMaxLen: # Save lines max length.
                vMaxLen = len(vElem)
        for x in range( len(self.vContent) ):
            self.vContent[x] = self.vContent[x].rjust( vMaxLen, Char ) # Adds extra characters.
        self.vContent = [ np.array([i for i in j],'U') for j in self.vContent ]
        #
        print( "Done aligning lines to left." )
        return self.vContent
        #
    #
    def Center( self, vInput, Char=' ' ):
        #
        if not self.__test_input(vInput): print( 'vInput is not a list of numpy ndarrays! Exiting function.' ) ; return
        #
        self.vContent = [ ''.join(i) for i in vInput ]
        vMaxLen = 0
        #
        for vElem in self.vContent:
            if len(vElem) > vMaxLen: # Save lines max length.
                vMaxLen = len(vElem)
        for x in range( len(self.vContent) ):
            self.vContent[x] = self.vContent[x].center( vMaxLen, Char ) # Adds extra characters.
        self.vContent = [ np.array([i for i in j],'U') for j in self.vContent ]
        #
        print( "Text centered." )
        return self.vContent
        #
    #
    def Crop( self, vInput, x1, y1, x2, y2 ):
        #
        if not self.__test_input(vInput): print( 'vInput is not a list of numpy ndarrays! Exiting function.' ) ; return
        #
        vRezCont = []
        Y = len(vInput)               # Y coord is stable. Only X coord can be variable.
        #
        for y in range(Y):            # For each line in file.
            if y >= y1 and y <= y2+1: # If y is between y1 and y2.
                vRezCont.append( vInput[y][x1:x2+1] ) # Add sliced line.
        self.vContent = vRezCont
        #
        print( "Done cropping text." )
        return self.vContent
        #
    #
    def Border( self, vInput, Char=' ', Thick=1 ):
        #
        if not self.__test_input(vInput): print( 'vInput is not a list of numpy ndarrays! Exiting function.' ) ; return
        #
        self.vContent = vInput
        for x in range( len(vInput) ):
            self.vContent[x] = np.array( Thick*[Char] + vInput[x].tolist() + Thick*[Char], 'U' )
        #
        L1 = len( self.vContent[0] )  # Lenght of first line.
        L2 = len( self.vContent[-1] ) # Lenght of last line.
        self.vContent = [np.array(L1*[Char],'U')] + self.vContent + [np.array(L2*[Char],'U')]
        #
        print( "Done adding full border." )
        return self.vContent
        #
    #
    def RightBorder( self, vInput, Char=' ', Thick=1 ):
        #
        if not self.__test_input(vInput): print( 'vInput is not a list of numpy ndarrays! Exiting function.' ) ; return
        #
        self.vContent = vInput
        for x in range( len(vInput) ):
            self.vContent[x] = np.array( Thick*[Char] + vInput[x].tolist(), 'U' )
        #
        print( "Done adding right border." )
        return self.vContent
        #
    #
    def LeftBorder( self, vInput, Char=' ', Thick=1 ):
        #
        if not self.__test_input(vInput): print( 'vInput is not a list of numpy ndarrays! Exiting function.' ) ; return
        #
        self.vContent = vInput
        for x in range( len(vInput) ):
            self.vContent[x] = np.array(vInput[x].tolist() + Thick*[Char], 'U' )
        #
        print( "Done adding left border." )
        return self.vContent
        #
    #

#
