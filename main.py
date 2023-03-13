from talon import Module, Context, canvas, ctrl, cron, ui, actions, app
from talon.types import Point2d

from .core.zone_refresher import *
from .core.display import *
from .core.display_drawer import DisplayDrawer
from .core.interaction_rule import InteractionRule
from .core.interaction_zone import InteractionZone
from .core.zone import *
from typing import Any, Union

zones = Module()

drawer = DisplayDrawer()
refresher = ZoneRefresher()
currentZones = {}

class ZoneConfiguration:
    def __init__(self, id: str,zone: Zone, display: Display) -> None:
        self.id = id
        self.zone = zone
        self.display = display
        pass

@zones.action_class
class ZonesActions:
    def add_zone(id: str, left: int, right: int, top: int, bottom: int, warmup: int, cooldown: Union[int,None], command: str):
        """Add Configuration"""
        global currentZones

        rz = RectangleZone(left,right,top,bottom)
        # Note: using actions.mimic() Is very bad practice! Don't use this!
        ir = InteractionRule(warmup,cooldown,lambda value: actions.mimic(command),id)
        d = RectangleDisplay()
        d.set_name(id)

        iz = InteractionZone(rz,ir,d)

        currentZones[id] = ZoneConfiguration(id,iz,d)
        
        pass

    def enable_zones():
        """enable zones"""
        global drawer
        global refresher
        global currentZones

        v = currentZones.values()
        for c in v:
            refresher.insert(c.zone,c.id)
            drawer.insert(c.display,c.id)

        refresher.refresh_over_millisecond_interval(20)
        drawer.enable()
        pass

    def disable_zones():
        """disable zones"""
        global drawer
        global refresher
        global currentZones

        refresher.stop()
        drawer.disable()

        refresher = ZoneRefresher()
        drawer = DisplayDrawer()
        currentZones = {}
        pass
