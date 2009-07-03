# -*- coding: latin-1 -*-
'''
Letter-Monster Engine v0.2.9
Copyright © 2009, Cristi Constantin. All rights reserved.
This module demonstrates all Backpack functions.
'''

import os, sys
import numpy as np
sys.path.insert( 0, os.getcwd() )
from _classes import Backpack

vInput = '''\
    .\n\
      xx   \n\
-012345     \n\
 this is 3\n\
-12345  E\n\
 this is 5\n\
 1234 6789 4321\n\
           xx\n\
/  \        \n\
  x   3 \n\
               |   |\n\
\n\
\n\
E O F ()     \n\
'''

_bp = Backpack()

vResult = _bp._Transform( 's2a', vInput ) # Transform string into Numpy Array.

vResult = _bp.Rotate90Right( vResult ) # Rotate, then undo.
vResult = _bp.Rotate90Left( vResult )

vResult = _bp.Reverse( vResult ) # Reverse content just for fun.
vResult = _bp.FlipH( vResult ) # Undo reverse...
vResult = _bp.FlipV( vResult )

vResult = _bp.AlignRight( vResult ) # Align right and left.
vResult = _bp.AlignLeft( vResult )

vResult = _bp.StripRightSpace( vResult ) # Strip spaces.
vResult = _bp.StripLeftSpace( vResult )

vResult = _bp.Center( vResult )

vResult = _bp.Border( vResult, Thick=2 ) # Border.
vResult = _bp.Crop( vResult, 1, 1, -1, -1 ) # Crop some border.

vResult = _bp.RightBorder( vResult, Char='~', Thick=1 )
vResult = _bp.LeftBorder( vResult, Char='~', Thick=1 )
vResult = _bp.Border( vResult, Char='#', Thick=2 )

print
print ''.join (np.hstack( np.hstack( (i,np.array([u'\n'],'U')) ) for i in vResult ))

os.system( 'echo Done.&pause' )

#
