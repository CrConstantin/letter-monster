
import os

f = open( os.getcwd() + '/unicode_table.txt', 'w', 1 )

#
for i in range(1, 65536):
    to_write = u'unicode %s / %s = %s\n' % ( str(i), str(hex(i)), unichr(i) )
    f.write( to_write.encode('utf_8') )
#

f.close() ; del f
