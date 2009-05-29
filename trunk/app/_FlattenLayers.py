
import numpy as np
from time import clock

#
def sort_zorder(x):
    return x.z
#
# TODO !!!!! Multiple transparent values !
# TODO !!!!! Move insert layers into given position !
#
def FlattenLayers( vInput ):
    '''
This function takes as input a dictionary containing layers, like LetterMonster.body.\n\
Only layers that have a "data" attribute (Raster and Vector) can be rendered.
Function returns the flatened result, as Rectangular Unicode Numpy Array.
'''
    #
    ti = clock()
    vOutput = np.zeros((1,1), 'U') # Define one empty Rectangular Unicode Numpy Array.
    #
    for vElem in sorted(vInput.values(), key=sort_zorder): # For all elements in LetterMonster body, sorted by Z-order...
        if (str(vElem)=='raster' and vElem.visible) or (str(vElem)=='vector' and vElem.visible): # If element is a visible Raster or Vector...
            vData = vElem.data          # This should be a Rectangular Unicode Numpy Array.
            vCoords = vElem.position    # This should be a tuple with 2 integers.
            vTransp = vElem.transparent # This should be a unicode character.
            #
            # Get maximum length between current Element array shape and current Output array shape.
            vCoord0 = max(vData.shape[0]+vCoords[0], vOutput.shape[0])
            vCoord1 = max(vData.shape[1]+vCoords[1], vOutput.shape[1])
            #
            # Resize Output Array to current layer array shape + current layer position.
            vOutput.resize( (vCoord0, vCoord1) )
            #
            # MASK 1 : all null values become transparent values.
            vMask = vData==u''
            vData[ vMask ] = vTransp
            #
            # MASK 2 : insert all NON-transparent values into Final Numpy Array, considering the position...
            vMask = vData!=vTransp
            vOutput[ vMask ] = vData[ vMask ]
            #
            del vMask # Just to make sure. :p
            #
        # If not Raster or Vector, pass.
    #
    tf = clock()
    print( 'Flatten Layers took %.4f seconds.' % (tf-ti) )
    return vOutput
    #
#
