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
    "This is helper functions class.\n\
    It uses no arguments for initialization."
    #
    def __init__(self):
        self.vContent = None
    #
    def __str__(self):
        '''String representation of this abstract class.'''
        return 'I am the Evil Backpack. Baaah!'
    #
    def StrToYamlNdarray( self, vInput, Transform=True ):
        #
        from bz2 import compress
        from yaml import dump, add_representer
        from _letter_monster import ndarray_repr
        add_representer(np.ndarray, ndarray_repr)
        #
        vCont = [ np.array([j for j in i],'U') for i in vInput.split('\n') ]
        #
        print( "Done transforming String to YAML !ndarray." )
        if Transform:
            return dump(data=vCont, width=99, indent=2, canonical=False, default_flow_style=False)
        else:
            return vCont
        #
    #
    def Rotate90Right( self, vInput, Compress=True ):
        #
        self.vContent = vInput.split('\n')
        self.vContent.reverse()
        #
        vMaxLen = 0
        for vElem in self.vContent:
            if len(vElem) > vMaxLen: # Save lines max length.
                vMaxLen = len(vElem)
        for x in range( len(self.vContent) ): # Add extra spaces to equalize.
            self.vContent[x] = self.vContent[x].rstrip().ljust(vMaxLen)
        #
        vRevCont = map( lambda *row: [elem for elem in row], *self.vContent ) # Rotate the square.
        #
        del self.vContent
        self.vContent = [ ''.join(vCont) for vCont in vRevCont ] # Join the sub-lists.
        if Compress:
            for x in range( len(self.vContent) ): # Remove extra spaces from the end of the lines.
                self.vContent[x] = self.vContent[x].rstrip()
        #
        print( "Done rotating 90 degrees right." )
        self.vContent = '\n'.join( self.vContent )
        return self.vContent
        #
    #
    def Rotate90Left( self, vInput, Compress=True ):
        #
        self.vContent = vInput.split('\n')
        #
        vMaxLen = 0
        for vElem in self.vContent:
            if len(vElem) > vMaxLen: # Save lines max length.
                vMaxLen = len(vElem)
        for x in range( len(self.vContent) ): # Add extra spaces to equalize.
            self.vContent[x] = self.vContent[x].rstrip().ljust(vMaxLen)
        #
        vRevCont = map( lambda *row: [elem for elem in row], *self.vContent ) # Rotate the square.
        #
        del self.vContent
        self.vContent = [ ''.join(vCont) for vCont in vRevCont ] # Join the sub-lists.
        if Compress:
            for x in range( len(self.vContent) ): # Remove extra spaces from the end of the lines.
                self.vContent[x] = self.vContent[x].rstrip()
        #
        self.vContent.reverse()
        print( "Done rotating 90 degrees left." )
        self.vContent = '\n'.join( self.vContent )
        return self.vContent
        #
    #
    def FlipH( self, vInput ):
        #
        self.vContent = vInput.split('\n')
        vRevCont = []
        #
        for vLine in self.vContent:
            vRevCont.append( vLine[::-1] ) # Reverse letters for each line.
        #
        print( "Done reversing letters for each line." )
        self.vContent = '\n'.join( vRevCont )
        return self.vContent
        #
    #
    def FlipV( self, vInput ):
        #
        self.vContent = vInput.split('\n')
        self.vContent.reverse() # First file line becomes last file line.
        #
        print( "Done reversing lines." )
        self.vContent = '\n'.join( self.vContent )
        return self.vContent
        #
    #
    def Reverse( self, vInput ):
        #
        self.vContent = vInput
        #
        self.vContent = self.vContent[::-1] # Reverse all content.
        print( "Done reversing content." )
        return self.vContent
        #
    #
    def StripRightSpace( self, vInput ):
        #
        self.vContent = vInput.split('\n')
        #
        for x in range( len(self.vContent) ): # Remove extra spaces from the end of the lines.
            self.vContent[x] = self.vContent[x].rstrip()
        #
        print( "Done striping right spaces for each line." )
        self.vContent = '\n'.join( self.vContent )
        return self.vContent
        #
    #
    def StripLeftSpace( self, vInput ):
        #
        self.vContent = vInput.split('\n')
        #
        for x in range( len(self.vContent) ): # Remove extra spaces from the start of the lines.
            self.vContent[x] = self.vContent[x].lstrip()
        #
        print( "Done striping left spaces for each line." )
        self.vContent = '\n'.join( self.vContent )
        return self.vContent
        #
    #
    def AlignRight( self, vInput, Char=' ' ):
        #
        self.vContent = vInput.split('\n')
        #
        vMaxLen = 0
        for vElem in self.vContent:
            if len(vElem) > vMaxLen: # Save lines max length.
                vMaxLen = len(vElem)
        for x in range( len(self.vContent) ):
            self.vContent[x] = self.vContent[x].ljust( vMaxLen, Char )
        #
        print( "Done aligning lines to right." )
        self.vContent = '\n'.join(self.vContent)
        return self.vContent
        #
    #
    def AlignLeft( self, vInput, Char=' ' ):
        #
        self.vContent = vInput.split('\n')
        #
        vMaxLen = 0
        for vElem in self.vContent:
            if len(vElem) > vMaxLen: # Save lines max length.
                vMaxLen = len(vElem)
        for x in range( len(self.vContent) ):
            self.vContent[x] = self.vContent[x].rjust( vMaxLen, Char )
        #
        print( "Done aligning lines to left." )
        self.vContent = '\n'.join(self.vContent)
        return self.vContent
        #
    #
    def Center( self, vInput, Char=' ' ):
        #
        self.vContent = vInput.split('\n')
        #
        vMaxLen = 0
        for vElem in self.vContent:
            if len(vElem) > vMaxLen: # Save lines max length.
                vMaxLen = len(vElem)
        for x in range( len(self.vContent) ):
            self.vContent[x] = self.vContent[x].center( vMaxLen, Char )
        #
        print( "Text centered." )
        self.vContent = '\n'.join(self.vContent)
        return self.vContent
        #
    #
    def Crop( self, vInput, x1, y1, x2, y2 ):
        #
        self.vContent = vInput.split('\n')
        vRezCont = []
        #
        Y = len(self.vContent)        # This is Y coord. The X coord can be variable.
        for y in range(Y):            # For each line in file.
            if y >= y1 and y <= y2+1: # If y is between y1 and y2.
                vRezCont.append( self.vContent[y][x1:x2+1] ) # Add sliced line.
        #
        print( "Done cropping text." )
        self.vContent = '\n'.join( vRezCont )
        return self.vContent
        #
    #
    def Border( self, vInput, Char=' ', Thick=1 ):
        #
        self.vContent = vInput.split('\n')
        #
        for x in range( len(self.vContent) ):
            self.vContent[x] = Thick*Char + self.vContent[x] + Thick*Char
        #
        L1 = len( self.vContent[0] )  # Lenght of first line.
        L2 = len( self.vContent[-1] ) # Lenght of last line.
        #
        ToReturn = Thick*(Char*L1 +'\n') + '\n'.join(self.vContent) +'\n'+ Thick*(Char*L2 +'\n')
        print( "Done adding full border." )
        self.vContent = ToReturn[:-1] # Return all except for the last character, a newline.
        return self.vContent
        #
    #
    def RightBorder( self, vInput, Char=' ', Thick=1 ):
        #
        self.vContent = vInput.split('\n')
        #
        for x in range( len(self.vContent) ):
            self.vContent[x] = Thick*Char + self.vContent[x]
        #
        print( "Done adding right border." )
        self.vContent = '\n'.join(self.vContent)
        return self.vContent
        #
    #
    def LeftBorder( self, vInput, Char=' ', Thick=1 ):
        #
        self.vContent = vInput.split('\n')
        #
        for x in range( len(self.vContent) ):
            self.vContent[x] = self.vContent[x] + Thick*Char
        #
        print( "Done adding left border." )
        self.vContent = '\n'.join(self.vContent)
        return self.vContent
        #
    #

#
