#  Letter Monster  #
#        v1        #
#    Main Class    #

import Image, ImageFilter
from os import getcwd                # Get currend directory.
from cStringIO import StringIO       # Used for StringIO algorithm.
from xml.dom.minidom import parse    # Used for reading XML data.
from xml.dom.minidom import Document # Used for creating XML data.
from time import clock               # Used for timing operations.
from psyco import full ; full ()     # Performance boost.

import sys ; sys.path.insert(0, getcwd() )
from _classes import * # Need to add current directory as path to import classes.

class LetterMonster:
    "This is the Letter Monster Class.\n\
    ^-^ You would have never guessed it.\n\
    It uses no arguments for initialization."
    #
    def __init__(self):
        #
        self.DEBUG = True
        #
        self.log = []        # All functions throw their messages in here.
        self.bp = Backpack() # Helper functions instance.
        self.data_types = ('raster', 'vector', 'event', 'macro')
        self.body = {}
        #
        self.visible_size = (100, 100)
        self.max_morph_rate = 1
        #
    #
#---------------------------------------------------------------------------------------------------
    #
    def __str__(self):
        '''String representation of the engine.'''
        return 'I am Letter Monster. Baaah!'
        #
    #
#---------------------------------------------------------------------------------------------------
    #
    def Hatch(self, visible_size=(100,100), max_morph_rate=1):
        '''Initialize the engine.'''
        self.visible_size = visible_size
        self.max_morph_rate = max_morph_rate
        #
    #
#---------------------------------------------------------------------------------------------------
    #
    def Consume(self, image='image.jpg', text='DooDoo.txt', x=0, y=0, pattern='default', filter='', algorithm='stringio'):
        '''Takes an image and transforms it into ASCII code.'''
        #
        try: vInput = Image.open( image )
        except: print( '"%s" is not a valid image path! Exiting function!' % image ) ; return
        try: vOutput = open( text, mode='w', buffering=-1 )
        except: print( '"%s" cannot be open for writing! Exiting function!' % text ) ; return
        #
        if x and not y:     # If x has a value.
            if self.DEBUG: print( "Resizing to X = %i." % x )
            y = (x * vInput.size[1]) / vInput.size[0]
            print( "Y becomes %i." % y )
        elif y and not x:   # Or if y has a value.
            if self.DEBUG: print( "Resizing to Y = %i." % y )
            x = (y * vInput.size[0]) / vInput.size[1]
            print( "X becomes %i." % x )
        #
        elif x and y:       # If both x and y have a value.
            if self.DEBUG: print( "Disproportionate resize X = %i, Y = %i." % ( x, y ) )
        if x or y:          # If resize was called.
            vInput = vInput.resize((x, y), Image.BICUBIC) # Do the resize.
        if filter:          # If filter was called.
            for filt in filter.split('|'):
                filt = filt.upper()
                if filt in ( 'BLUR', 'SMOOTH', 'SMOOTH_MORE', 'DETAIL', 'SHARPEN',
                            'CONTOUR', 'EDGE_ENHANCE', 'EDGE_ENHANCE_MORE' ):
                    vInput = vInput.filter( getattr(ImageFilter, filt) )
                    print( "Applied %s filter." % filt )
                else:
                    print( '"%s" is not a valid fliter! Filter ignored.' % filt )
            #
        #
        Patterns = {
        'default'    : u'&80$21|;:\' ',                        # Original Patrick T. Cossette pattern
        'cro'        : u'MWBHASI+;,. ',                        # Cristi Constantin pattern
        'dos'        : u'\u2588\u2593\u2592\u2665\u2666\u263b\u256c\u263a\u25ca\u25cb\u2591 ', # Cristi Constantin DOS pattern.
        'sharp'      : u'#w4Axv^*\"\'` ',                      # Cristi Constantin Sharp
        'smooth'     : u'a@\u00a9\u0398O90c\u00a4\u2022. ',    # Cristi Constantin Smooth
        'vertical'   : u'\u00b6\u0132I|}\u00ce!VAi; ',         # Cristi Constantin Vertical
        'horizontal' : u'\u25ac\u039e\u00ac\u2261=\u2248~-. ', # Cristi Constantin Horizontal
        'numbers'    : u'0684912357',
        'letters'    : u'NADXEIQOVJL ',
        }

        if pattern.lower() in Patterns.keys():
            vPattern = Patterns[pattern.lower()]
        else:
            print( '"%s" is not a valid pattern! Using default pattern.' % pattern )
            vPattern = Patterns['default']
        #
        if algorithm=='stringio':
            file_str = StringIO()
        elif algorithm=='listappend':
            vResult = []
        else:
            print( '"%s" is not a valid algorithm! Using default algorithm.' % algorithm )
            algorithm = 'stringio'
            file_str = StringIO()

        ti = clock()
        if self.DEBUG: print( "Starting spawn..." )
        #
        if algorithm=='stringio':
            #
            vLen = len( vPattern )
            #
            for py in range( vInput.size[1] ): # Cycle through the image's pixels, one by one
                file_str.write( '\n' )
                for px in xrange( vInput.size[0] ):
                    #
                    RGB = vInput.getpixel((px, py))   # Retrieve pixel RGB values
                    vColor = RGB[0] + RGB[1] + RGB[2] # Find the general darkness of the pixel
                    #
                    for vp in range( vLen ): # For each element in the string pattern...
                        if vColor <= ( 255 * 3 / vLen * (vp+1) ): # Return matching character from pattern.
                            file_str.write( vPattern[vp].encode('utf8') )
                            break
                        elif vColor > ( 255 * 3 / vLen * vLen ) and vColor <= ( 255 * 3 ): # If not in range, return last character from pattern.
                            file_str.write( vPattern[-1].encode('utf8') )
                            break
                        #
                    #
                #
            vOutput.write( file_str.getvalue() ) # Write the ASCII result to file.
            #self.body = file_str.getvalue().split('\n')
            file_str.close() ; del file_str
        #
        elif algorithm=='listappend':
            #
            vLen = len( vPattern )
            #
            for py in range(vInput.size[1]): # Cycle through the image's pixels, one by one
                #
                vTempRez = []
                #
                for px in range(vInput.size[0]):
                    RGB = vInput.getpixel((px, py))   # Retrieve pixel RGB values
                    vColor = RGB[0] + RGB[1] + RGB[2] # Find the general darkness of the pixel
                    #
                    for vp in range( vLen ): # For each element in the string pattern...
                        if vColor <= ( 255 * 3 / vLen * (vp+1) ): # Return matching character from pattern.
                            vTempRez.append( vPattern[vp].encode('utf8') )
                            break
                        elif vColor > ( 255 * 3 / vLen * vLen ) and vColor <= ( 255 * 3 ): # If not in range, return last character from pattern.
                            vTempRez.append( vPattern[-1].encode('utf8') )
                            break
                        #
                    #
                #
                vResult.append( ''.join( vTempRez ) )
                #
            vOutput.write( '\n'.join( vResult ) ) # Write the ASCII result to file.
            #self.body = vResult
            del vResult

        tf = clock()
        if self.DEBUG: print( 'Done.\nTransformation took %.4f seconds.' % (tf-ti) )
        #
        del vInput
        vOutput.close() ; del vOutput
        #
    #
#---------------------------------------------------------------------------------------------------
    #
    def Bite(self, lmgl):
        '''Load a LMGL (Letter Monster Graphical Letters) file.\n\
        All defined class variables are loaded from XML, all extra variables in XML are ignored.'''
        try: vInput = open( lmgl )
        except: print( '"%s" is not a valid LMGL path! Exiting!' % lmgl ) ; return
        vInput.close ; del vInput
        #
        try: vLmgl = parse( lmgl )
        except: print( '"%s" cannot be parsed! Invalid XML file! Exiting function!' % lmgl ) ; return
        #
        for data_type in self.data_types: # For each type (raster, vector, event, macro)
            #
            for xml in vLmgl.getElementsByTagName(data_type):
                #
                if data_type=='raster':
                    Elem = Raster()
                elif data_type=='vector':
                    Elem = Vector()
                elif data_type=='event':
                    Elem = Event()
                elif data_type=='macro':
                    Elem = Macro()
                #
                name = xml.getAttribute('name')
                #
                for Attr in [ v for v in dir(Elem) if '__' not in v ]: # For each variable in current class...
                    setattr( Elem, Attr, xml.getAttribute(Attr) ) # Set a value from LMGL to that variable.
                    print Attr, '=', xml.getAttribute(Attr) # Display all data.
                #
                if name and (not getattr(self, name, 0)): # If element has a name and name is not taken.
                    self.body[str(name)] = Elem # After loading all data, store the element in LM dict.
                else:
                    print( '"%s" is invalid name, or already exists! Exiting function' % name )
                    return
                #
            #
        #
    #
#---------------------------------------------------------------------------------------------------
    #
    def Spawn(self, lmgl):
        '''Save changes into a LMGL (Letter Monster Graphical Letters) file.'''
        try:
            vInput = open( lmgl )
            print( '"%s" is a valid LMGL file! Will not overwrite. Exiting!' % lmgl ) ; return
        except: pass # If file exists, pass.
        #
        LmglDoc = Document()                     # Creating document.
        lmglRoot = LmglDoc.createElement('lmgl') # Creating LMGL root.
        lmglRoot.setAttribute('version','1')
        #
        for vv in sorted(self.body.values()):
            lmglChild = LmglDoc.createElement( str(vv) ) # Create child type of data.
            for key, val in sorted(vars( vv ).items()):  # For each class instance in body, get pairs : var name, var value.
                lmglChild.setAttribute(key, val) # Append name and value in LMGL.
            lmglRoot.appendChild( lmglChild )
        #
        LmglDoc.appendChild( lmglRoot )
        vInput = open( lmgl, 'w' )
        vInput.write( LmglDoc.toprettyxml() )
        vInput.close() ; del vInput
    #
#---------------------------------------------------------------------------------------------------
    #
    def Feed(self):
        '''Connect to a LMGL (Letter Monster Graphical Letters) file.\n\
    Everytime a Morph happens, the LMGL file is updated on hard disk.'''
        pass
    #
#---------------------------------------------------------------------------------------------------
    #
    def Morph(self): # Mutate
        '''Moves the internal engine layers, thus making Spit (Render) return different images.'''
        pass
    #
#---------------------------------------------------------------------------------------------------
    #
    def Spit(self):
        '''Render function. Returns the current reprezentation of the engine.'''
        pass
    #

#
