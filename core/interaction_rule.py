from .display import Display
from typing import Any, Union
from talon import cron

class InteractionRule:
    def __init__(self, warmup: int, cooldown: Union[int, None], action, name):
        self.action = action
        self.warmup = warmup#how long does it need to be inside
        self.cooldown = cooldown
        self.job = None
        self.reset_state()
        self.interaction_value = None
        self.name = name
        self.display = None
    
    def set_display(self, display: Display):
        self.display = display
        self.display.set_name(self.name)
    
    def react_to_mouse_position(self, is_inside_zone: bool, interaction_value: Any):
        if is_inside_zone:
            self.handle_mouse_position_inside_zone(interaction_value)
        else:
            self.reset_state()

    def reset_state(self):
        self.cancel_asynchronous_tasks()
        self.should_warm_up_on_interaction = True
        self.ready_to_perform_action = False
    
    def cancel_asynchronous_tasks(self, interaction_completed = False):
        if self.job:
            cron.cancel(self.job)
            self.job = None
            if not interaction_completed:
                self.display.handle_interaction_canceled()
    
    def handle_mouse_position_inside_zone(self, interaction_value):
        self.interaction_value = interaction_value
        if self.job is None:
            time_until_next_action = self.compute_time_until_next_action_call()
            self.display.handle_interaction_start(time_until_next_action)
            if time_until_next_action is not None:
                self.job = cron.after(f'{time_until_next_action}ms', self.complete_interaction)

    def compute_time_until_next_action_call(self):
        if self.should_warm_up_on_interaction:
            return self.warmup
        return self.cooldown

    def complete_interaction(self):
        self.cancel_asynchronous_tasks(interaction_completed = True)
        self.ready_to_perform_action = True
        self.should_warm_up_on_interaction = False
        self.action(self.interaction_value)
        self.display.handle_interaction_completed()

    def should_perform_action(self):
        return self.ready_to_perform_action