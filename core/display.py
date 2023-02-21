from .zone import Zone

class Display:
    def __init__(self):
        self.name = ''
        self.zone = None

    def set_name(self, name: str):
        self.name = name

    def set_zone(self, zone: Zone):
        self.zone = zone

    def handle_interaction_start(self, time_limit_on_next_action_call):
        pass

    def handle_interaction_canceled(self):
        pass

    def handle_interaction_completed(self):
        pass

class PrintoutDisplay(Display):
    def handle_interaction_start(self, time_limit_on_next_action_call):
        print(f'{self.name}: interaction start with time limit {time_limit_on_next_action_call}')
    
    def handle_interaction_canceled(self):
        print(f'{self.name}: interaction canceled')
    
    def handle_interaction_completed(self):
        print(f'{self.name}: interaction completed')