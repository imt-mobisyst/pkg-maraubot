import sys
sys.path.insert( 1, __file__.split('tests')[0] )
# ------------------------------------------------------------------------ #
#                 T E S T   p y B b M m  : :  C O D E                      #
# ------------------------------------------------------------------------ #
import src.maraubotmap as mbm

def test_world_init():
    world= mbm.World()
    assert type(world) == mbm.World
