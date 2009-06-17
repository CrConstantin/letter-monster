# -*- coding: latin-1 -*-
'''
    Letter-Monster Engine v0.2.2 \n\
    Copyright © 2009, Cristi Constantin. All rights reserved. \n\
    This module contains Flatten Layers function. \n\
'''

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
Only layers that have a "data" attribute (Raster and Vector) can be rendered.\n\
Function returns the flatened result, as Rectangular Unicode Numpy Array.\n\
'''
    #
    ti = clock()
    #
    # If Body has one layer, return it. There is nothing to flatten.
    if len(vInput)==1:
        tf = clock()
        print( 'Flatten Layers took %.4f seconds.' % (tf-ti) )
        return vInput.values()[0].data
    #
    S0 = 0 ; S1 = 0
    # Save maxim shape values for all layers.
    for vElem in vInput.values():
        if (str(vElem)=='raster' and vElem.visible) or (str(vElem)=='vector' and vElem.visible):
            if vElem.data.shape[0]<=1 and vElem.data.shape[1]<=1: continue # Ignore empty arrays.
            S0 = max( S0, vElem.data.shape[0]+vElem.offset[0] )
            S1 = max( S1, vElem.data.shape[1]+vElem.offset[1] )
    #
    # Create a big empty array for all other arrays to fit in.
    vOutput = np.zeros( (S0, S1), 'U' )
    del S0, S1
    #
    for vElem in sorted(vInput.values(), key=sort_zorder): # For all elements in LetterMonster body, sorted by Z-order...
        if (str(vElem)=='raster' and vElem.visible) or (str(vElem)=='vector' and vElem.visible): # If element is a visible Raster or Vector...
            #
            # Some pointers...
            vData = vElem.data          # This should be a Rectangular Unicode Numpy Array.
            vDataShape = vData.shape    # Element data shape.
            vOffset = vElem.offset      # This should be a list with 2 integers. First value is down, second value is right.
            #
            if vElem.transparent:       # If there are transparent characters...
                # All "transparent characters" from current Layer Data become empty strings.
                for vT in vElem.transparent:
                    vMask = vData==vT
                    vData[ vMask ] = u''
                #
            #
            # Mask == all NON-empty characters.
            vMask = vData!=u''
            #
            # Insert all NON-empty values into Final Numpy Array, considering the position.
            vOutput[ vOffset[0]:vDataShape[0]+vOffset[0], vOffset[1]:vDataShape[1]+vOffset[1]][ vMask ] = vData[ vMask ]
            del vMask # Just to make sure. :p
            #
        # If not Raster or Vector, pass.
    #
    tf = clock()
    print( 'Flatten Layers took %.4f seconds.' % (tf-ti) )
    return vOutput
    #
#
