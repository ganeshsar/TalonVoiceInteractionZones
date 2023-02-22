from .interaction_zone import InteractionZone
from talon import ctrl
from talon import cron

class ZoneRefresher:
    def __init__(self):
        self.zones = {}
        self.job = None
    
    def insert(self, zone: InteractionZone, identifier: str):
        if identifier in self.zones:
            self.cancel_zone_asynchronous_tasks(identifier) 
        self.zones[identifier] = zone
    
    def remove(self, identifier: str):
        if identifier in self.zones:
            self.cancel_zone_asynchronous_tasks(identifier)
            del self.zones[identifier]

    def cancel_zone_asynchronous_tasks(self, identifier):
        zone: InteractionZone = self.zones[identifier]
        zone.cancel_asynchronous_tasks()

    def refresh(self):
        horizontal, vertical = ctrl.mouse_pos()
        for zone in self.zones:
            self.zones[zone].react_to_mouse_position(horizontal, vertical)
    
    def refresh_over_millisecond_interval(self, milliseconds: int):
        self.stop()
        self.job = cron.interval(f'{milliseconds}ms', self.refresh)

    def stop(self):
        if self.job:
            cron.cancel(self.job)