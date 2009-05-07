
import os, sys
sys.path.insert( 0, os.getcwd() )
from _letter_monster import LetterMonster

#

lm = LetterMonster()
lm.DEBUG = True

#lm.Consume( image='..\\Behind_Your_Illusion_by_littlemewhatever.jpg', text='Example_Consume.txt', x=0, y=175, pattern='sharp', filter='detail' )
#lm.Consume( image='..\\Chimpance__by_faboarts.jpg', text='Example_Consume.txt', x=0, y=175, pattern='smooth', filter='blur' )
#lm.Consume( image='..\\Robot_chicken_by_net_surfer.jpg', text='Example_Consume.txt', x=0, y=175, pattern='cro', filter='smooth_more' )
#lm.Consume( image='..\\Sunstone_by_nmsmith.jpg', text='Example_Consume.txt', x=0, y=175, pattern='letters', filter='smooth|detail|smooth|sharpen' )
#lm.Consume( image='..\\Waiting_for_Godot_by_humanskin.jpg', text='Example_Consume.txt', x=0, y=175, pattern='numbers', filter='smooth' )
#lm.Consume( image='..\\Wind_by_pincel3d.jpg', text='Example_Consume.txt', x=0, y=175, pattern='dos', filter='smooth' )

#lm.Consume( image='..\\So_fragile_____by_Prahaai.jpg', text='Example_Consume.txt', x=0, y=175, pattern='sharp', filter='detail' )
#lm.Consume( image='..\\Ana_by_Prahaai.jpg', text='Example_Consume.txt', x=0, y=175, pattern='sharp', filter='smooth|detail' )
#lm.Consume( image='..\\garbov_by_Arukasme.jpg', text='Example_Consume.txt', x=0, y=175, pattern='standard', filter='sharp|smooth' )

lm.Consume( image='../Moon.jpg', x=0, y=0, pattern='dos' )

try: os.remove( 'test_lmgl_c.yaml' )
except: pass
lm.Save( 'test_lmgl_c.yaml' )

#

print( "Please, use Lucida Console Bold, size 4 for viewing." )

#

print( 'Finished.\n' )
os.system( 'pause' )

#
