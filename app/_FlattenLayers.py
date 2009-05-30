
import numpy as np
from time import clock

#
def sort_zorder(x):
    return x.z
#

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
            vCoords = vElem.position    # This should be a list with 2 integers.
            vTransp = vElem.transparent # This should be unicode characters, or null string.
            #
            # Save Element data shape.
            vShape0 = vData.shape[0]
            vShape1 = vData.shape[1]
            #
            # Get maximum length between current Element data shape and current Output data shape.
            vCoord0 = max(vShape0+vCoords[0], vOutput.shape[0])
            vCoord1 = max(vShape1+vCoords[1], vOutput.shape[1])
            #
            # Resize Output data to current layer data shape + current layer position.
            vOutput.resize( (vCoord0, vCoord1) )
            #
            if vTransp: # If there are transparent characters...
                # All "transparent characters" become empty strings.
                for vT in vTransp:
                    vMask = vData==vT
                    vData[ vMask ] = u''
                #
            #
            # Insert all NON-empty values into Final Numpy Array, considering the position.
            vMask = vData!=u''
            vOutput[ vCoords[0]:vShape0+vCoords[0], vCoords[1]:vShape1+vCoords[1]][ vMask ] = vData[ vMask ]
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
