from .zone import Zone
from .interaction_rule import InteractionRule
from .display import Display

class InteractionZone:
    def __init__(self, zone: Zone, interaction_rule: InteractionRule, display: Display):
        self.zone = zone
        self.display = display
        self.interaction_rule = interaction_rule
        self.set_display(display)

    def set_zone(self, zone: Zone):
        self.zone = zone
        self.display.set_zone(zone)
    
    def set_display(self, display: Display):
        self.display = display
        self.display.set_zone(self.zone)
        self.interaction_rule.set_display(display)

    def set_interaction_rule(self, rule: InteractionRule):
        self.interaction_rule.cancel_asynchronous_tasks()
        self.interaction_rule = rule
        self.interaction_rule.set_display(self.display)
    
    def cancel_asynchronous_tasks(self):
        self.interaction_rule.cancel_asynchronous_tasks()
    
    def react_to_mouse_position(self, horizontal, vertical):
        is_in_zone = self.zone.contains_position(horizontal, vertical)
        interaction_value = None
        if is_in_zone:
            interaction_value = self.zone.compute_interaction_value(horizontal, vertical)
        self.interaction_rule.react_to_mouse_position(is_in_zone, interaction_value)