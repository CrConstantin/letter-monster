
import os, sys
sys.path.insert( 0, os.getcwd() )
from _letter_monster import Backpack

#

vInput = open( 'To_Test.txt', 'r' )
vOutput = open( 'Example_Strip+Center+Border.txt', 'w' )

_bp = Backpack()
vResult = vInput.read()

vResult = _bp.Rotate90Right( vResult )
vResult = _bp.Rotate90Left( vResult )
vResult = _bp.Reverse( vResult )
vResult = _bp.Reverse( vResult )

vResult = _bp.AlignRight( vResult )
vResult = _bp.AlignLeft( vResult )

vResult = _bp.StripLeftSpace( vResult )
vResult = _bp.StripRightSpace( vResult )

vResult = _bp.Center( vResult )
vResult = _bp.Border( vResult )
vResult = _bp.Border( vResult, Char='#', Thick=2 )

vOutput.write( vResult )

#

print( 'Finished.\n' )
os.system( 'pause' )

#
