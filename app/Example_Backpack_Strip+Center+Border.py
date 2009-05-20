
import os, sys
import numpy as np
from pprint import pprint
sys.path.insert( 0, os.getcwd() )
from _classes import Backpack

#

vInput = open( 'To_Test.txt', 'r' )
vOutput = open( 'Example_Strip+Center+Border.txt', 'w' )

_bp = Backpack()
print( 'Starting to read example file...\n' )
vResult = _bp.StrToArray( vInput.read() )
vInput.close()

vResult = _bp.Rotate90Right( vResult ) # Rotate, then undo.
vResult = _bp.Rotate90Left( vResult )

vResult = _bp.Reverse( vResult ) # Reverse, then undo.
vResult = _bp.FlipH( vResult )
vResult = _bp.FlipV( vResult )

vResult = _bp.AlignRight( vResult ) # Align right and left.
vResult = _bp.AlignLeft( vResult )

vResult = _bp.StripLeftSpace( vResult ) # Strip spaces.
vResult = _bp.StripRightSpace( vResult )

vResult = _bp.Center( vResult )

vResult = _bp.Border( vResult ) # Border.
vResult = _bp.RightBorder( vResult, Char='~' )
vResult = _bp.LeftBorder( vResult, Char='~' )
vResult = _bp.Border( vResult, Char='#', Thick=2 )

vOutput.write( '\n'.join([ ''.join([j.encode('utf8') for j in i]) for i in vResult ]) )
vOutput.close()

#

print( 'Finished.\n' )
os.system( 'pause' )

#
