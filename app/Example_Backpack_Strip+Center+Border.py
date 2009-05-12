
import os, sys
sys.path.insert( 0, os.getcwd() )
from _classes import Backpack

#

vInput = open( 'To_Test.txt', 'r' )
vOutput = open( 'Example_Strip+Center+Border.txt', 'w' )

_bp = Backpack()
print( 'Starting to read example file...\n' )
vResult = vInput.read()


vResult = _bp.Rotate90Right( vResult ) # Rotate, then undo.
vResult = _bp.Rotate90Left( vResult )

vResult = _bp.Reverse( vResult ) # Reverse, then undo.
vResult = _bp.Reverse( vResult )

vResult = _bp.AlignRight( vResult ) # Align right and left.
vResult = _bp.AlignLeft( vResult )

vResult = _bp.StripLeftSpace( vResult ) # Strip spaces.
vResult = _bp.StripRightSpace( vResult )

vResult = _bp.Center( vResult ) # Center.
vResult = _bp.Border( vResult ) # Border.
vResult = _bp.RightBorder( vResult, Char='~' )
vResult = _bp.LeftBorder( vResult, Char='~' )
vResult = _bp.Border( vResult, Char='#', Thick=2 )


vOutput.write( vResult )

#

print( 'Finished.\n' )
os.system( 'pause' )

#
