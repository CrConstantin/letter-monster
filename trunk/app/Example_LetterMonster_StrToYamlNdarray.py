
import os, sys
sys.path.insert( 0, os.getcwd() )
from _classes import Backpack

#

b = Backpack()

vInput = open( 'Str_2_Yaml.txt', 'w' )
vInput.write( b.StrToYamlNdarray('Raster\n000000000\nx x x data') )
vInput.close()

#

print( 'Finished.\n' )
os.system( 'pause' )

#
