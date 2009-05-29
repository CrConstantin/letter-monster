
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
All layers data is merged and the function returns the result as 2D unicode numpy array.
'''
    #
    tti = clock()
    vOutput = [[]]
    #
    for vElem in sorted(vInput.values(), key=sort_zorder): # For each visible Raster and Vector in body, sorted in Z-order.
        if (str(vElem)=='raster' and vElem.visible) or (str(vElem)=='vector' and vElem.visible):
            Data = vElem.data                 # This is a 2D numpy array.
            #
            for nr_row in range( len(Data) ): # For each row in Data.
                #
                NData = Data[nr_row]     # New data, to be written over old data. It's a 1D unicode numpy array.
                NData = NData[NData!=''] # Strip empty strings from the end.
                OData = vOutput[nr_row:nr_row+1] or [[]] # Old data. First loops is empty list, then is 1D unicode numpy array.
                OData = OData[0] # It doesn't work other way.
                #
                vLN = len(NData)
                vLO = len(OData)
                #
                # Replace all NData transparent pixels with OData, at respective indices.
                vMask = (NData==vElem.transparent)[:vLO]
                try: NData[ vMask ] = OData[ vMask ]
                except: pass
                #
                if vLN >= vLO:
                    # If new data is longer than old data, old data will be completely overwritten.
                    TempB = np.copy(NData)
                    vOutput[nr_row:nr_row+1] = [TempB]
                    del TempB
                else: # Old data is longer than new data ; old data cannot be null.
                    TempB = np.copy(OData)
                    TempB[:vLN] = NData
                    vOutput[nr_row:nr_row+1] = [TempB]
                    del TempB
                #
            #
        # If not Raster or Vector, pass.
    #
    ttf = clock()
    print( 'Flatten layers took %.4f seconds.' % (ttf-tti) )
    return vOutput
    #

#
