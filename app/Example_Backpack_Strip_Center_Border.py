
import os, sys
import numpy as np
sys.path.insert( 0, os.getcwd() )
from _classes import Backpack

#

vInput = open( 'To_Test.txt', 'r' )
vOutput = open( 'Example_Backpack.txt', 'w' )

_bp = Backpack()
print( 'Starting to read example file...\n' )
vResult = _bp._Transform( 's2a', vInput.read() )
vInput.close()

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

vOutput.write( ''.join (np.hstack( np.hstack( (i,np.array([u'\n'],'U')) ) for i in vResult )).encode('utf8') )
vOutput.close()

#

print( 'Finished.\n' )
os.system( 'pause' )

#
