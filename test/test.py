  

from ..core.zone_refresher import *
from ..core.display import *
from ..core.display_drawer import DisplayDrawer
from ..core.interaction_rule import InteractionRule
from ..core.interaction_zone import InteractionZone
from ..core.zone import *
from talon import actions
TESTING = False
if TESTING:
    upper_left = RectangleZone(10, 310, 10, 310)
    up_rule = InteractionRule(1000, 500, lambda value: actions.key('up'), 'up')
    up_display = RectangleDisplay()
    up_display.set_name('up')
    up_zone = InteractionZone(upper_left, up_rule, up_display)   
     
    upper_right = RectangleZone(1920-310, 1910, 10, 310)
    down_rule = InteractionRule(200, 2000, lambda value: actions.key(f'down:{int(value.get_percentage_up()*10)}'), 'down')
    down_display = RectangleDisplay()
    down_display.set_name('down')
    down_zone = InteractionZone(upper_right, down_rule, down_display)
    
    refresher = ZoneRefresher()
    refresher.insert(up_zone, 'up')
    refresher.insert(down_zone, 'down')
    refresher.refresh_over_millisecond_interval(20)
    
    drawer = DisplayDrawer()
    drawer.insert(up_display, 'up')
    drawer.insert(down_display,'down')
    drawer.enable()
