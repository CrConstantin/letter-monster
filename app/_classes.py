#  Letter Monster  #
#        v1        #
#  Helper Classes  #

class Raster:
    "Raster objects class"
    #
    def __init__(self):
        self.name = None
        self.data = None
        self.origin = '0,0'
        self.visible = False
        self.lock = False
    #
    def __str__(self):
        '''String representation.'''
        return 'raster'
    #
#

class Vector:
    "Vector objects class"
    #
    def __init__(self):
        self.name = None
        self.data = None
        self.origin = '0,0'
        self.visible = False
        self.lock = False
    #
    def __str__(self):
        '''String representation.'''
        return 'vector'
    #
#

class Event:
    "Event objects class"
    #
    def __init__(self):
        self.name = None
        self.data = None
        self.affect_macro = None
    #
    def __str__(self):
        '''String representation.'''
        return 'event'
    #
#

class Macro:
    "Macro objects class"
    #
    def __init__(self):
        self.name = None
        self.data = None
    #
    def __str__(self):
        '''String representation.'''
        return 'macro'
    #
#

class Backpack:
    "This is helper functions class."
    #
    def __init__(self):
        self.vContent = None
    #
    def __str__(self):
        '''String representation of this abstract class.'''
        return 'I am the Evil Backpack. Baaah!'
    #
    def __repr__(self):
        '''Scientific representation of this abstract class.'''
        return 'I am scientific Evil Backpack. Baaah!'
    #
    def Rotate90Right( self, vInput, Compress=True ):
        print( "Starting Rotation to Right..." )
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
        print( "Rotated 90 degrees right." )
        self.vContent = '\n'.join( self.vContent )
        return self.vContent
    #
    def Rotate90Left( self, vInput, Compress=True ):
        print( "Starting Rotation to Left..." )
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
        print( "Rotated 90 degrees left." )
        self.vContent = '\n'.join( self.vContent )
        return self.vContent
    #
    def FlipH( self, vInput ):
        print( "Starting Horizontal Flip..." )
        #
        self.vContent = vInput.split('\n')
        vRevCont = []
        #
        for vLine in self.vContent:
            vRevCont.append( vLine[::-1] )  # Reverse letters for each line.
        #
        print( "Reversed letters for each line." )
        self.vContent = '\n'.join( vRevCont )
        return self.vContent
    #
    def FlipV( self, vInput ):
        print( "Starting Vertical Flip..." )
        #
        self.vContent = vInput.split('\n')
        self.vContent.reverse() # First file line becomes last file line.
        #
        print( "All lines reversed." )
        self.vContent = '\n'.join( self.vContent )
        return self.vContent
    #
    def Reverse( self, vInput ):
        print( "Starting Reverse..." )
        #
        self.vContent = vInput
        #
        self.vContent = self.vContent[::-1] # Reverse all content.
        print( "Content reversed." )
        return self.vContent
    #
    def StripRightSpace( self, vInput ):
        print( "Starting Strip Right Spaces..." )
        #
        self.vContent = vInput.split('\n')
        #
        for x in range( len(self.vContent) ): # Remove extra spaces from the end of the lines.
            self.vContent[x] = self.vContent[x].rstrip()
        #
        print( "Right spaces striped for each line." )
        self.vContent = '\n'.join( self.vContent )
        return self.vContent
    #
    def StripLeftSpace( self, vInput ):
        print( "Starting Strip Left Spaces..." )
        #
        self.vContent = vInput.split('\n')
        #
        for x in range( len(self.vContent) ): # Remove extra spaces from the start of the lines.
            self.vContent[x] = self.vContent[x].lstrip()
        #
        print( "Left spaces striped for each line." )
        self.vContent = '\n'.join( self.vContent )
        return self.vContent
    #
    def AlignRight( self, vInput, Char=' ' ):
        print( "Starting Align Right..." )
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
        print( "Lines aligned right." )
        self.vContent = '\n'.join(self.vContent)
        return self.vContent
    #
    def AlignLeft( self, vInput, Char=' ' ):
        print( "Starting Align Left..." )
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
        print( "Lines aligned left." )
        self.vContent = '\n'.join(self.vContent)
        return self.vContent
    #
    def Center( self, vInput, Char=' ' ):
        print( "Starting Centre text..." )
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
    def Crop( self, vInput, x1, y1, x2, y2 ):
        print( "Starting Crop..." )
        #
        self.vContent = vInput.split('\n')
        vRezCont = []
        #
        Y = len(self.vContent)             # This is Y coord. The X coord can be variable.
        for y in range(Y):            # For each line in file.
            if y >= y1 and y <= y2+1: # If y is between y1 and y2.
                vRezCont.append( self.vContent[y][x1:x2+1] ) # Add sliced line.
        #
        print( "String croped." )
        self.vContent = '\n'.join( vRezCont )
        return self.vContent
    #
    def Border( self, vInput, Char=' ', Thick=1 ):
        print( "Starting Border Full..." )
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
        print( "Added full border." )
        self.vContent = ToReturn[:-1] # Return all except for the last character, a newline.
        return self.vContent
    #
    def RightBorder( self, vInput, Char=' ', Thick=1 ):
        print( "Starting Right Border..." )
        #
        self.vContent = vInput.split('\n')
        #
        for x in range( len(self.vContent) ):
            self.vContent[x] = Thick*Char + self.vContent[x]
        #
        print( "Added right border." )
        self.vContent = '\n'.join(self.vContent)
        return self.vContent
    #
    def LeftBorder( self, vInput, Char=' ', Thick=1 ):
        print( "Starting Right Border..." )
        #
        self.vContent = vInput.split('\n')
        #
        for x in range( len(self.vContent) ):
            self.vContent[x] = self.vContent[x] + Thick*Char
        #
        print( "Added right border." )
        self.vContent = '\n'.join(self.vContent)
        return self.vContent
    #

#
