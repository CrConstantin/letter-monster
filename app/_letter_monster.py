#  Letter Monster  #
#        v1        #
#    Main Class    #

import Image, ImageFilter            # PIL Image.
from os import getcwd                # OS get currend directory.
from os import system as cmd         # OS command line access.
import numpy as np                   # Numpy arrays.
from cPickle import dump, load       # Represent letter-monster body.
from bz2 import BZ2File              # Compress and write data.
from time import clock               # Timing operations.
from psyco import full ; full ()     # Performance boost.
import sys ; sys.path.insert(0, getcwd() ) # Save current dir in path.
from _classes import * # Need to add curr dir as path to import classes.

print 'I am Python r29!'

#
def sort_zorder(x):
    return x.z
#

class LetterMonster:
    '''
This is the Letter Monster Class. ^-^ You would have never guessed it.\n\
It uses no arguments for initialization. You can later on setup the engine via Hatch function.'''
    #
    def __init__(self):
        #
        self.DEBUG = True
        #
        self.body = {}
        self.max_morph_rate = 1
        self.visible_size = (100, 100)
        self.bp = Backpack() # Helper functions instance.
        #
        self.data_types = ('raster', 'vector', 'event', 'macro')
        self.Patterns = {
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
        '''Setup the engine.'''
        self.visible_size = visible_size
        self.max_morph_rate = max_morph_rate
        #
    #
#---------------------------------------------------------------------------------------------------
    #
    def Load(self, lmgl):
        '''Load a LMGL (Letter Monster Graphical Letters) file, using cPickle.'''
        try: vInput = BZ2File( lmgl, 'r', 0, 6 ) # Load for reading, no buffer, compress level 6.
        except: print( '"%s" is not a valid path! Exiting function!' % lmgl ) ; return
        #
        ti = clock()
        try: vLmgl = load( vInput )
        except: print( '"%s" cannot be parsed! Invalid cPickle file! Exiting function!' % lmgl ) ; return
        self.body = vLmgl
        vInput.close() ; del vInput
        tf = clock()
        #
        if self.DEBUG: print( 'Loading LMGL took %.4f seconds total.' % (tf-ti) )
        #
    #
#---------------------------------------------------------------------------------------------------
    #
    def Save(self, lmgl):
        '''Save body into a LMGL (Letter Monster Graphical Letters) file, using cPickle.'''
        try:
            vInput = open( lmgl )
            print( '"%s" is a LMGL file! Will not overwrite. Exiting function!' % lmgl ) ; return
        except: pass # If file exists, pass.
        #
        ti = clock()
        vInput = BZ2File( lmgl, 'w', 0, 6 ) # Load for writing, no buffer, compress level 6.
        dump( self.body, vInput, 2 ) # Represent as cPickle method 2.
        vInput.close() ; del vInput
        tf = clock()
        #
        if self.DEBUG: print( 'Saving LMGL took %.4f seconds total.' % (tf-ti) )
        #
    #
#---------------------------------------------------------------------------------------------------
    #
    def _execute(self, object):
        '''Automatically execute object instructions. "Object" must be the name of a data structure.'''
        #
        try:
            vElem = self.body[object]
            vInstructions = vElem.instructions
        except: print( '"%s" object doesn\'t have instructions, or doesn\'t exist! Exiting execute!' % object ) ; return
        #
        if not vInstructions:
            print( '"%s" has null instructions! Exiting execute!' % object ) ; return
        #
        ti = clock()
        if str(vElem)=='vector':
            for vInstr in vInstructions: # For each dictionary in the instructions list.
                vFunc = vInstr['f']      # Save the function to call, then delete this mapping.
                del vInstr['f']
                #
                f = getattr(self.bp, vFunc, 'Error') # Save the function call.
                #
                if f!='Error': # If function is not Error, means it's valid.
                    #
                    # Overwrite the name of the layer with the data of the layer.
                    try: vInstr['vInput'] = self.body[vInstr['vInput']].data
                    except: print( '"%s" doesn\'t have valid data! Call ignored!' % vInput ) ; continue
                    #
                    # Try to call the function with parameters and catch the errors.
                    try: vData = f( **vInstr )
                    except TypeError: print( 'Incorrect arguments for function "%s"! Call ignored!' % vFunc ) ; continue
                    except: print( 'Unknown error occured in "%s" function call! Call ignored!' % vFunc ) ; continue
                    #
                    # Explode data back.
                    if vData: self.body[object].data = vData
                    else: self.body[object].data = []
                    #
                else:
                    print( 'Function "%s" doesn\'t exist! Call ignored!' % vFunc )
                #
        else:
            print( 'Instructions for "%s" object not yet implemented!' % str(vElem) ) ; return
        #
        tf = clock()
        if self.DEBUG: print( 'Execute took %.4f seconds.' % (tf-ti) )
        #
    #
#---------------------------------------------------------------------------------------------------
    #
    def Consume(self, image='image.jpg', x=0, y=0, pattern='default', filter=''):
        '''Takes an image as input, transforms it into Unicode Ndarrays and stores it internally.'''
        #
        try: vInput = Image.open( image )
        except: print( '"%s" is not a valid image path! Exiting function!' % image ) ; return
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
        del x ; del y
        #
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
        if pattern.lower() in self.Patterns:
            vPattern = self.Patterns[pattern.lower()]
        else:
            print( '"%s" is not a valid pattern! Using default pattern.' % pattern )
            vPattern = self.Patterns['default']
        #
        ti = clock() # Global counter.
        tti = clock() # Local counter.
        #
        vResult = np.empty( (vInput.size[1],vInput.size[0]), 'U' )
        if self.DEBUG: print( "Starting consume..." )
        #
        vLen = len( vPattern )
        getpx = vInput.getpixel
        #
        for py in range(vInput.size[1]): # Cycle through the image's pixels, one by one
            #
            for px in range(vInput.size[0]):
                #
                RGB = getpx((px, py))             # Retrieve pixel RGB values
                vColor = RGB[0] + RGB[1] + RGB[2] # Find the general darkness of the pixel
                #
                for vp in range( vLen ):                      # For each element in the string pattern...
                    if vColor <= ( 255 * 3 / vLen * (vp+1) ): # Return matching character from pattern.
                        vResult[py,px] = vPattern[vp]
                        break
                    elif vColor > ( 255 * 3 / vLen * vLen ) and vColor <= ( 255 * 3 ): # If not in range, return last character from pattern.
                        vResult[py,px] = vPattern[-1]
                        break
                #
            #
        #
        ttf = clock()
        if self.DEBUG: print( 'Transformation took %.4f seconds.' % (ttf-tti) )
        for x in range(1, 999):
            if not 'raster'+str(x) in self.body: # If "raster+x" doesn't exist.
                vElem = Raster()
                vElem.name = 'raster'+str(x)
                vElem.data = vResult
                vElem.visible = True
                vElem.lock = False
                self.body['raster'+str(x)] = vElem # Save raster in body.
                del vElem
                break
            #
        #
        del vResult ; del vInput
        tf = clock()
        #
        if self.DEBUG: print( 'Consume took %.4f seconds total.' % (tf-ti) )
        #
    #
#---------------------------------------------------------------------------------------------------
    #
    def Spit(self, format='WIN CMD', transparent=' '):
        '''
Render function. Represents engine body.\n\
All visible Raster and Vector layers are rendered.'''
        #
        vOutput = [[]]
        #
        for vElem in sorted(self.body.values(), key=sort_zorder): # For each visible Raster and Vector in body, sorted in Z-order.
            if (str(vElem)=='raster' and vElem.visible) or (str(vElem)=='vector' and vElem.visible):
                Data = vElem.data                 # This is a list of numpy ndarrays.
                #
                for nr_row in range( len(Data) ): # For each numpy ndarray (row) in Data.
                    #
                    NData = Data[nr_row]                     # New data, to be written over old data.
                    OData = vOutput[nr_row:nr_row+1] or [[]] # This is old data. Can be numpy ndarray, or empty list.
                    OData = OData[0]
                    #
                    # Replace all NData transparent pixels with OData, at respective indices.
                    try: NData[ (NData==transparent)[:len(OData)] ] = OData[ (NData==transparent)[:len(OData)] ]
                    except: pass
                    #
                    if len(NData) >= len(OData): 
                        # If new data is longer than old data, old data will be completely overwritten.
                        vOutput[nr_row:nr_row+1] = [NData]
                    else: # Old data is longer than new data ; old data cannot be null.
                        TempB = np.copy(OData)
                        TempB.put( range(len(NData)), NData )
                        vOutput[nr_row:nr_row+1] = [TempB]
                        del TempB
                    #
                #
            # If not Raster or Vector, pass.
        #
        if format=='WIN CMD':
            for vLine in vOutput:
                vEcho = u''.join(u'^'+i for i in vLine)
                if vEcho: cmd( '@ECHO %s' % vEcho.encode('utf') )
                else: cmd( '@ECHO.' )
            #
        # More formats will be implemented soon.
    #
#---------------------------------------------------------------------------------------------------
    #
    def Spawn(self, lmgl=None, out='txt', filename='Out', transparent=u' '):
        '''
Export function. Saves engine body on Hard Disk in specific format.\n\
Can also transform one LMGL into : TXT, Excel, or HTML, without changing engine body.'''
        ti = clock() # Global counter.
        if lmgl: # If a LMGL file is specified, export only the LMGL, don't change self.body.
            tti = clock() # Local counter.
            try: vInput = BZ2File( lmgl, 'r', 0, 6 ) # Load for reading, no buffer, compress level 6.
            except: print( '"%s" is not a valid path! Exiting function!' % lmgl ) ; return
            #
            try: vLmgl = load( vInput )
            except: print( '"%s" cannot be parsed! Invalid cPickle file! Exiting function!' % lmgl ) ; return
            #
            vInput.close() ; del vInput
            ttf = clock()
            if self.DEBUG: print( 'Loading LMGL (Spawn) took %.4f seconds.' % (ttf-tti) )
        else: vLmgl = self.body
        #
        out = out.lower() # Lower letters.
        if out not in ('txt', 'csv', 'html'):
            print( '"%s" is not a valid export type! Exiting function!' % out ) ; return
        #
        tti = clock() # Local counter.
        TempA = [[]]
        #
        for vElem in sorted(vLmgl.values(), key=sort_zorder): # For each visible Raster and Vector in body, sorted in Z-order.
            if (str(vElem)=='raster' and vElem.visible) or (str(vElem)=='vector' and vElem.visible):
                Data = vElem.data                 # This is a list of numpy ndarrays.
                #
                for nr_row in range( len(Data) ): # For each numpy ndarray (row) in Data.
                    #
                    NData = Data[nr_row]                   # New data, to be written over old data.
                    OData = TempA[nr_row:nr_row+1] or [[]] # This is old data. Can be numpy ndarray, or empty list.
                    OData = OData[0]
                    #
                    # Replace all NData transparent pixels with OData, at respective indices.
                    try: NData[ (NData==transparent)[:len(OData)] ] = OData[ (NData==transparent)[:len(OData)] ]
                    except: pass
                    #
                    if len(NData) >= len(OData): 
                        # If new data is longer than old data, old data will be completely overwritten.
                        TempA[nr_row:nr_row+1] = [NData]
                    else: # Old data is longer than new data ; old data cannot be null.
                        TempB = np.copy(OData)
                        TempB[0:len(NData)] = NData
                        TempA[nr_row:nr_row+1] = [TempB]
                        del TempB
                    #
                #
            # If not Raster or Vector, pass.
        #
        ttf = clock()
        print( 'Overwriting data took %.4f seconds.' % (ttf-tti) )
        #
        tti = clock() # Local counter.
        vOut = open( filename+'.'+out, 'w' ) # Filename + Extension.
        if out=='txt':
            vOut.write( ''.join ( np.hstack( np.hstack( (i,np.array([u'\n'],'U')) ) for i in TempA # Concatenate all arrays with an array containing ['\n'].
                                           )
                                ).encode('utf8')
                      )
        #
        elif out=='csv':
            vOut.write( '"\n'.join('",'.join('"%s' % j for j in i) for i in TempA) ) # Put each value into " ", pairs.
            vOut.write( '"\n' )
        #
        elif out=='html':
            vOut.write('<html>\n<body>\n<table border="0" cellpadding="0" cellspacing="0" style="font-family: Lucida Console, Courier New; font-size: 3px; font-weight: bold; letter-spacing: 1px;">\n<tr>')
            vOut.write( '</td></tr>\n<tr>'.join('</td>'.join('<td>%s' % j for j in i) for i in TempA) ) # Put each value into <td> </td> pairs.
            vOut.write('</td></tr>\n</table>\n</body>\n</html>')
        #
        vOut.close() ; del TempA ; del vOut
        ttf = clock()
        if self.DEBUG: print( 'Unite arrays and lists took %.4f seconds.' % (ttf-tti) )
        #
        tf = clock()
        if self.DEBUG: print( 'Spawn took %.4f seconds total.' % (tf-ti) )
        #
    #

#
