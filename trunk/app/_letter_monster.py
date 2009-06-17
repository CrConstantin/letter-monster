# -*- coding: latin-1 -*-
'''
    Letter-Monster Engine v0.2.2 \n\
    Copyright © 2009, Cristi Constantin. All rights reserved. \n\
    This module contains Letter-Monster class with all its functions. \n\
'''

import os, sys                   # Important System functions.
import Image, ImageFilter        # Python-Imaging.
import ImageFont, ImageDraw      # Python-Imaging.
import numpy as np               # Numpy arrays.
import cPickle, yaml             # YAML and cPickle.
from yaml import CLoader as Loader
from yaml import CDumper as Dumper
from yaml import add_representer, add_constructor
import zlib, gzip, bz2           # Compress and decompress data.
from time import clock           # Timing operations.
sys.path.insert(0, os.getcwd() ) # Save current dir in path.

try: from psyco import profile ; profile() # Performance boost.
except: pass                               # If Psyco is not available, pass.
from _classes import *
from _FlattenLayers import FlattenLayers

print 'I am LM r45!'

#
# Define YAML represent for numpy ndarray.
def ndarray_repr(dumper, data):
    return dumper.represent_scalar(u'!array', zlib.compress(data.dumps(), 7).decode('latin_1'))
add_representer(np.ndarray, ndarray_repr)
#
# Define YAML construct data for numpy ndarray.
def ndarray_construct(loader, node):
    return np.loads(zlib.decompress(loader.construct_scalar(node).encode('latin_1')))
add_constructor(u'!array', ndarray_construct)
#

class LetterMonster:
    '''
This is Letter-Monster Class. You would have never guessed it, right? ^_^\n\
It uses no arguments for initialization.\n\
'''
    #
    def __init__(self):
        '''
Initializes the engine.\n\
LetterMonster -> DEBUG. If False, debug messages will not be printed.\n\
LetterMonster -> body. This dictionary contains all layers loaded from LMGL and saved into LMGL.\n\
LetterMonster -> max_morph_rate. TODO.\n\
LetterMonster -> visible_size. TODO\n\
LetterMonster -> bp. It's a Backpack instance. All helper functions can be accessed through it.\n\
LetterMonster -> data_types. List with all valid layer names.\n\
LetterMonster -> Filters. List with all valid filter names, used in Consume function.\n\
LetterMonster -> Patterns. List with all valid pattern names, used in Consume function.\n\
'''
        #
        self.DEBUG = True
        #
        self.body = {}
        self.max_morph_rate = 1
        self.visible_size = (100, 100)
        self.bp = Backpack() # Helper functions instance.
        #
        self.data_types = ('raster', 'vector', 'event', 'macro')
        self.Filters = ( 'BLUR', 'SMOOTH', 'SMOOTH_MORE', 'DETAIL', 'SHARPEN', # All valid filters.
                         'CONTOUR', 'EDGE_ENHANCE', 'EDGE_ENHANCE_MORE' )
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
        '''String representation of the engine. It's just a fun function to have.\n'''
        return 'I am Letter-Monster! Be afraid! Baaah!'
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
        '''
Load a LMGL (Letter-Monster Graphical Letters) file.\n\
LMGL file format is nothing more than a YAML dump of LetterMonster body, compressed with BZ2.\n\
'''
        try:
            vInput = open( lmgl ) # Opening the file just to read first 3 characters.
            v3 = vInput.read(3)
            vInput.close() ; del vInput
        except: print( 'Letter-Monster snarls: "`%s` is not a valid path!"' % lmgl ) ; return 1
        #
        ti = clock()
        #
        if v3=='\x1f\x8b\x08': # LMGL file is GZIP format. Only cPickle is saved in here.
            vInput = gzip.open( lmgl, 'r', 8 )
            if self.DEBUG: print( 'Letter-Monster says: "Found GZIP cPickle."' )
            #
            try: vLmgl = cPickle.load( vInput )
            except: print( 'Letter-Monster snarls: "`%s` file cannot be parsed by cPickle! Failed to load."' % lmgl ) ; return 1
        #
        elif v3=='BZh':        # LMGL file is BZ2 format.
            vInput = bz2.BZ2File( lmgl, 'r', 0, 8 )
            if self.DEBUG: print( 'Letter-Monster says: "Found BZ2 cPickle or YAML."' )
            success = False
            #
            try: vLmgl = cPickle.load( vInput ) ; success = True
            except: pass
            if not success:
                vInput.seek(0)
                try: vLmgl = yaml.load( vInput )
                except: print( 'Letter-Monster snarls: "`%s` file is neither cPickle, nor YAML! Failed to load."' % lmgl ) ; return 1
        #
        elif v3=='---':        # LMGL file is raw YAML.
            vInput = open( lmgl, 'rb', 0 )
            if self.DEBUG: print( 'Letter-Monster says: "Found raw YAML."' )
            #
            try: vLmgl = yaml.load( vInput )
            except: print( 'Letter-Monster snarls: "`%s` file cannot be parsed by YAML! Failed to load."' % lmgl ) ; return 1
        #
        else: # If not GZIP, BZ2, or YAML...
            print( 'Letter-Monster snarls: "`%s` canoot be opened! It\'s neither GZIP, BZ2 or YAML!"' % lmgl ) ; return 1
        #
        self.body = vLmgl # On load, old body is COMPLETELY overwritten.
        vInput.close() ; del vInput
        self.__validate()
        #
        tf = clock()
        if self.DEBUG: print( 'Letter-Monster says: "Loading LMGL took %.4f seconds total."' % (tf-ti) )
        #
    #
#---------------------------------------------------------------------------------------------------
    #
    def Save(self, lmgl, mode='p:gzip'):
        '''
Save body into a LMGL (Letter-Monster Graphical Letters) file.\n\
Valid modes are : p:gzip (cPickle in gzip file), p:bz2 (cPickle in bz2 file), y:bz2 (YAML in bz2 file), y (YAML).\n\
You should also check Load function.\n\
'''
        try:
            vInput = open( lmgl )
            print( 'Letter-Monster snarls: "`%s` is a LMGL file! I refuse to overwrite!"' % lmgl ) ; return 1
        except: pass # If file exists, pass.
        #
        ti = clock()
        #
        if mode=='p:gzip':
            vInput = gzip.open( lmgl, 'w', 8 )
            cPickle.dump(self.body, vInput, 2)
        #
        elif mode=='p:bz2':
            vInput = bz2.BZ2File( lmgl, 'w', 0, 8 )
            cPickle.dump(self.body, vInput, 2)
        #
        elif mode=='y:bz2':
            vInput = bz2.BZ2File( lmgl, 'w', 0, 8 )
            yaml.dump(self.body, stream=vInput, width=125, indent=2, canonical=False, default_flow_style=False,
                explicit_start=True, explicit_end=True)
        #
        elif mode=='y':
            vInput = open( lmgl, 'w', 0 )
            yaml.dump(self.body, stream=vInput, width=125, indent=2, canonical=False, default_flow_style=False,
                explicit_start=True, explicit_end=True)
        #
        else: print( 'Letter-Monster snarls: "`%s` is not a valid mode to save LMGL files!"' % mode ) ; return 1
        #
        vInput.close() ; del vInput
        self.__validate()
        tf = clock()
        if self.DEBUG: print( 'Letter-Monster says: "Saving LMGL took %.4f seconds total."' % (tf-ti) )
        #
    #
#---------------------------------------------------------------------------------------------------
    #
    def __validate(self):
        '''
Private validation function. After load or save, each LMGL file MUST be validated.\n\
Errors are printed in console, but cannot be fixed. It is your responsability to do the fixing.\n\
Valid LMGL file should respect this:\n\
 - internal name of all layers must be the same as the key used to acces them, in LetterMonster body.\n\
 - data of Raster and Vector layers must be Rectangular Numpy Arrays.\n\
 - instructions of Vector and Macro layers must be lists of dictionaries.\n\
 - offset of Raster and Vector layers must be tuples of 2 integers.\n\
 - transparent of Raster and Vector layers must be a unicode string.\n\
'''
        #
        body = self.body
        #
        if not body:
            print( 'Letter-Monster snarls: "My body is empty! I have nothing to validate."' ) ; return
        #
        for vKey, vElem in body.items():
            if vKey!=vElem.name: # If body name is not the same as internal object name...
                print( 'Letter-Monster growls: "Be warned! Inside my body, %s object label is ambiguous! Body name is `%s` and object name is `%s`!"'
                    % (str(vElem),vKey,vElem.name) )
            #
            try: # Try to get information about object data.
                if not ( str(type(vElem.data))=="<type 'numpy.ndarray'>" and str(type(vElem.data[0]))=="<type 'numpy.ndarray'>" ):
                    print( 'Letter-Monster growls: "Be warned! %s object `%s` data is not a valid rectangular Numpy Array!"'
                        % (str(vElem),vKey) )
            except: pass # If object doesn't have "data", pass.
            #
            try: # Try to get information about object instructions.
                if not ( (str(type(vElem.instructions))=="<type 'list'>" or str(type(vElem.instructions))=="<type 'tuple'>")
                and str(type(vElem.instructions[0]))=="<type 'dict'>" ):
                    print( 'Letter-Monster growls: "Be warned! %s object `%s` instructions is not a valid list of dictionaries!"'
                        % (str(vElem),vKey) )
            except: pass # If object doesn't have "instructions", pass.
            #
            try: # Try to get information about objects offset.
                if not ( (str(type(vElem.offset))=="<type 'list'>" or str(type(vElem.offset))=="<type 'tuple'>")
                and str(type(vElem.offset[0]))=="<type 'int'>" and len(vElem.offset)==2 ):
                    print( 'Letter-Monster growls: "Be warned! %s object `%s` offset is not a list with two integers!"'
                        % (str(vElem),vKey) )
            except: pass # If object doesn't have "offset", pass.
            #
            try: # Try to get information about object transparent.
                if not str(type(vElem.transparent))=="<type 'unicode'>":
                    print( 'Letter-Monster growls: "Be warned! %s object `%s` transparent is not a unicode string!"'
                        % (str(vElem),vKey) )
            except: pass # If object doesn't have "transparent", pass.
            #
        #
    #
#---------------------------------------------------------------------------------------------------
    #
    def _execute(self, object):
        '''Execute instructions stored inside Vector or Macro layers. "Object" must be the name of a LatterMonster layer 
that containins instructions.\n'''
        #
        try:
            vElem = self.body[object]
            vInstructions = vElem.instructions
        except: print( 'Letter-Monster snarls: "`%s` is not an object from my body, or it doesn\'t have valid instructions! I refuse to execute!"' % object ) ; return
        #
        if not vInstructions:
            print( 'Letter-Monster growls: "`%s` has NULL instructions! I refuse to execute!"' % object ) ; return
        #
        ti = clock()
        if str(vElem)=='vector': # Execute vector instructions.
            for vInstr in vInstructions: # For each dictionary in vector instructions list.
                vFunc = vInstr['f']      # Save function name, then delete this mapping.
                del vInstr['f']          # All vector function calls are backpack functions.
                #
                f = getattr(self.bp, vFunc, 'Error') # Save the function call.
                #
                if f!='Error': # If function is not Error, means it's valid.
                    #
                    # Overwrite the Name of the vector with the Data of the vector.
                    try: vInstr['Input'] = self.body[vInstr['Input']].data
                    except: print( 'Letter-Monster growls: "Vector `%s` doesn\'t have valid data! Call ignored!"' % object ) ; continue
                    #
                    # Try to call the function with parameters and catch the errors.
                    try: vData = f( **vInstr )
                    except TypeError: print( 'Letter-Monster growls: "Incorrect arguments for function `%s`! Call ignored!"' % vFunc ) ; continue
                    except: print( 'Letter-Monster growls: "Unknown error occured in `%s` function call! Call ignored!"' % vFunc ) ; continue
                    #
                    # Save data in LetterMonster body -> object.
                    if vData is not None: self.body[object].data = vData
                    else: self.body[object].data = np.zeros((1,1),'U')
                    #
                else:
                    print( 'Letter-Monster growls: "I refuse to execute that! Vector `%s` tries to call function `%s` which doesn\'t exist!"'
                        % (object,vFunc) ) ; return
                #
            #
        if str(vElem)=='macro':
            pass
        else:
            print( 'Letter-Monster sighs: "Instructions for macros not yet implemented! Scheduled for version 0.3."' ) ; return
        #
        tf = clock()
        if self.DEBUG: print( 'Letter-Monster says: "Execute took %.4f seconds."' % (tf-ti) )
        #
    #
#---------------------------------------------------------------------------------------------------
    #
    def Consume(self, image='image.jpg', x=0, y=0, pattern='default', filter=''):
        '''
Takes a supported image as input, transforms it into a Rectangular Unicode Array and stores the result 
in LetterMonster body.\n\
You can use different patterns for transforming : default, cro, dos, sharp, smooth, vertical, horizontal, numbers, letters.\n\
You can also apply filters : BLUR, SMOOTH, SMOOTH_MORE, DETAIL, SHARPEN, CONTOUR, EDGE_ENHANCE, EDGE_ENHANCE_MORE.\n\
Later, you can export this "consumed" image into TXT, CSV, HTM, or whatever suits your needs, with Spawn, 
or you can Save its representation as LMGL.\n\
'''
        #
        try: vInput = Image.open( image )
        except:
            print( 'Letter-Monster snarls: "`%s` is not a valid image path, or Python-Imaging cannot open that type of file! Cannot consume!"'
                % image ) ; return
        #
        if x and not y:     # If x has a value.
            if self.DEBUG: print( 'Letter-Monster says: "I\'m resizing to X = %i."' % x )
            y = (x * vInput.size[1]) / vInput.size[0]
            if self.DEBUG: print( 'Letter-Monster says: "Y becomes %i."' % y )
        elif y and not x:   # Or if y has a value.
            if self.DEBUG: print( 'Letter-Monster says: "I\'m resizing to Y = %i."' % y )
            x = (y * vInput.size[0]) / vInput.size[1]
            if self.DEBUG: print( 'Letter-Monster says: "X becomes %i."' % x )
        #
        elif x and y:       # If both x and y have a value.
            if self.DEBUG: print( 'Letter-Monster says: "Disproportionate resize X = %i, Y = %i."' % (x,y) )
        if x or y:          # If resize was called.
            vInput = vInput.resize((x, y), Image.BICUBIC) # Do the resize.
        del x ; del y
        #
        if filter: # If filter was called.
            for filt in filter.split('|'):
                filt = filt.upper()
                if filt in self.Filters:
                    vInput = vInput.filter( getattr(ImageFilter, filt) )
                    if self.DEBUG: print( 'Letter-Monster says: "Applied %s filter."' % filt )
                else:
                    print( 'Letter-Monster growls: "I don\'t know any filter called `%s`! I will ignore it."' % filt )
            #
        #
        if pattern.lower() in self.Patterns:
            vPattern = self.Patterns[pattern.lower()]
        else:
            print( 'Letter-Monster growls: "I don\' know any pattern called `%s`! I will use default pattern."' % pattern )
            vPattern = self.Patterns['default']
        #
        ti = clock() # Global counter.
        tti = clock() # Local counter.
        #
        vResult = np.empty( (vInput.size[1],vInput.size[0]), 'U' )
        if self.DEBUG: print( 'Letter-Monster says: "Starting consume..."' )
        #
        vLen = len( vPattern )
        pxaccess = vInput.load()
        ch = len(vInput.getbands())
        #
        for py in range(vInput.size[1]): # Cycle through the image's pixels, one by one
            #
            for px in range(vInput.size[0]):
                #
                vColor = sum( pxaccess[px,py] ) # Calculate general darkness of the pixel.
                #
                for vp in range( vLen ):                       # For each element in the string pattern...
                    if vColor <= ( 255 * ch / vLen * (vp+1) ): # Return matching character from pattern.
                        vResult[py,px] = vPattern[vp]
                        break
                    elif vColor > ( 255 * ch / vLen * vLen ) and vColor <= ( 255 * ch ): # If not in range, return last character from pattern.
                        vResult[py,px] = vPattern[-1]
                        break
                #
            #
        #
        ttf = clock()
        if self.DEBUG: print( 'Letter-Monster says: "Transformation took %.4f seconds."' % (ttf-tti) )
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
        if self.DEBUG: print( 'Letter-Monster says: "Consume took %.4f seconds total."' % (tf-ti) )
        #
    #
#---------------------------------------------------------------------------------------------------
    #
    def Spit(self, format='CMD', autoclear=False):
        '''
Frame-by-frame render function. Represents LetterMonster body.\n\
All visible Raster and Vector layers are flattened and the result is sent to the specified output.\n\
Valid outputs are : CMD, SH.\n\
'''
        #
        if not format in ('CMD', 'SH'):
            print( 'Letter-Monster snarls: "Cannot spit in `%s` format! Exiting!"' % format )
        #
        try: vOutput = FlattenLayers( self.body )
        except: print( 'Letter-Monster snarls: "Flatten body layers returned an error! Cannot spit!"' )
        #
        if format=='CMD':
            if autoclear: vCmd = ['cls'] # If autoclear, clear the screen.
            else: vCmd = []
            #
            for vLine in vOutput:
                vEcho = u''.join(u'^'+i for i in u''.join(vLine))
                if vEcho: vCmd.append( 'echo %s' % vEcho.encode('utf8') )
                else: vCmd.append( 'echo.' )
            os.system( '&'.join(vCmd) ) # Execute Windows command!
            #
        elif format=='SH':
            if autoclear: vCmd = ['clear'] # If autoclear, clear the screen.
            else: vCmd = []
            #
            for vLine in vOutput:
                vEcho = u''.join(u'\\'+i for i in u''.join(vLine))
                if vEcho: vCmd.append( 'echo %s' % vEcho.encode('utf8') )
                else: vCmd.append( 'echo.' )
            os.system( '&&'.join(vCmd) ) # Execute Linux command!
            #
    #
#---------------------------------------------------------------------------------------------------
    #
    def Render(self, format='pygame'):
        '''
Render in a loop function. Represents LetterMonster body.\n\
All visible Raster and Vector layers are flattened and the result is sent to the specified output.\n\
Valid outputs are : pygame and pyglet.\n\
'''
        #
        if not format in ('pygame', 'pyglet'):
            print( 'Letter-Monster snarls: "Cannot render in `%s` format! Exiting!"' % format )
        #
        try: vOutput = FlattenLayers( self.body )
        except: print( 'Letter-Monster snarls: "Flatten body layers returned an error! Cannot render!"' )
        #
        if format=='pygame': # Pygame render.
            try: import pygame
            except: print( 'Letter-Monster snarls: "Could not import Pygame! Make sure you downloaded and installed it. Check http://www.pygame.org. Exiting!"' )
            pygame.init()
            #
            vSize = width, height = 320, 240
            vScreen = pygame.display.set_mode(vSize)
            vFont = pygame.font.SysFont('Lucida Console', 12)
            vHeight = vFont.get_height()
            #
            while 1:
                for event in pygame.event.get():
                    if event.type in (pygame.QUIT, pygame.KEYDOWN):
                        print( 'Letter-Monster says: "Key pressed, exiting..."' )
                        pygame.quit() ; return
                    #
                    i = 1
                    for vLine in vOutput:
                        vFR = vFont.render(''.join(vLine), True, (0,255,255))
                        vScreen.blit(vFR, (1,i))
                        i += vHeight
                    pygame.display.flip()
                #
            #
        elif format=='pyglet': # Pyglet render.
            try: import pyglet
            except: print( 'Letter-Monster snarls: "Could not import Pyglet! Make sure you downloaded and installed it. Check http://www.pyglet.org. Exiting!"' )
            #
            window = pyglet.window.Window(width=800, height=600, caption='Pyglet render', resizable=False, style=None, fullscreen=False, visible=True, vsync=True)
            label = pyglet.text.Label( text=''.join ( np.hstack( np.hstack( (i,np.array([u'\n'],'U')) ) for i in vOutput ) ).encode('utf8'),
                font_name='Lucida Console', font_size=8, x=1, y=window.height-1, width=len(vOutput[0]), anchor_x='left', anchor_y='top', multiline=True)
            #
            @window.event
            def on_key_press(symbol, modifiers):
                print( 'Letter-Monster says: "Key pressed, exiting..."' )
                window.close()
            @window.event
            def on_draw():
                window.clear()
                label.draw()
            #
            pyglet.app.run()
            #
        #
        # More formats will be implemented soon.
    #
#---------------------------------------------------------------------------------------------------
    #
    def Spawn(self, lmgl=None, out='txt', filename='Out'):
        '''
Export function. Saves engine body on Hard Disk, or transforms one LMGL into a specified format.\n\
Valid formats are : txt, csv, html, bmp, gif, jpg, png.\n\
'''
        #
        ti = clock() # Global counter for function.
        if lmgl: # If a LMGL file is specified, export only the LMGL, but don't change self.body.
            #
            vOldBody = self.body
            ret = self.Load( lmgl )
            if ret: return 1
            #
        #
        vLmgl = self.body # Save body...
        out = out.lower() # Lower letters.
        if out not in ('txt', 'csv', 'html', 'bmp', 'gif', 'jpg', 'png'):
            print( 'Letter-Monster growls: "I cannot export in `%s` type! Exiting spawn!' % out ) ; return 1
        #
        #try: 
        vOutput = FlattenLayers( vLmgl )
        #except: print( 'Letter-Monster snarls: "Flatten body layers returned an error! Cannot spawn!"' )
        #
        tti = clock() # Local counter.
        #
        if out=='txt':
            vOut = open( filename+'.'+out, 'w' ) # Filename + Extension.
            vOut.write( ''.join ( np.hstack( np.hstack( (i,np.array([u'\n'],'U')) ) for i in vOutput # Concatenate all arrays with an array containing ['\n'].
                                           )
                                ).encode('utf8')
                      )
            vOut.close()
        #
        elif out=='csv':
            vOut = open( filename+'.'+out, 'w' ) # Filename + Extension.
            vOut.write( '"\n'.join('",'.join('"%s' % j for j in i) for i in vOutput) ) # Put each value into " ", pairs.
            vOut.write( '"\n' )
            vOut.close()
        #
        elif out=='html':
            vOut = open( filename+'.'+out, 'w' ) # Filename + Extension.
            vOut.write('<html>\n<body>\n<table border="0" cellpadding="0" cellspacing="0" style="font-family: Lucida Console, Courier New; font-size: 3px; font-weight: bold; letter-spacing: 1px;">\n<tr>')
            vOut.write( '</td></tr>\n<tr>'.join('</td>'.join('<td>%s' % j for j in i) for i in vOutput) ) # Put each value into <td> </td> pairs.
            vOut.write('</td></tr>\n</table>\n</body>\n</html>')
            vOut.close()
        #
        elif out in ('bmp', 'gif', 'jpg', 'png'):
            lenW = len(vOutput[0]) # Get vOutput width and height.
            lenH = len(vOutput)
            vFont = ImageFont.truetype('c:/windows/fonts/lucon.ttf', 8) # Load font.
            vLtrSize = (vFont.getsize('x')[0], int(2*vFont.getsize('x')[1]/3))          # Get true size of a letter drawn with this font.
            vOut = Image.new('RGB', ((lenW+1)*vLtrSize[0],lenH*vLtrSize[1]), "#ffffee") # New image: Type, Width, Height, Background.
            vDraw = ImageDraw.Draw(vOut)
            i = 1
            for line in vOutput: # For each line...
                vDraw.text((1,i), ''.join ( line ).encode('utf8'), fill="#000066", font=vFont) # Draw line.
                i += vLtrSize[0]-1
            del i
            vOut.save( filename+'.'+out )
        #
        # More export formats will be implemented ...
        #
        del vOutput ; del vOut
        if lmgl:
            self.body = vOldBody # Restore old Body.
        #
        ttf = clock()
        if self.DEBUG: print( 'Letter-Monster says: "Exporting data took %.4f seconds."' % (ttf-tti) )
        tf = clock()
        if self.DEBUG: print( 'Letter-Monster says: "Spawn took %.4f seconds total."' % (tf-ti) )
        #
    #

#
