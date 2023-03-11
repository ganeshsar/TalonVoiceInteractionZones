from .zone import *
from talon.skia import Paint, Rect

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
    
    def draw(self, canvas):
        pass

class PrintoutDisplay(Display):
    def handle_interaction_start(self, time_limit_on_next_action_call):
        print(f'{self.name}: interaction start with time limit {time_limit_on_next_action_call}')
    
    def handle_interaction_canceled(self):
        print(f'{self.name}: interaction canceled')
    
    def handle_interaction_completed(self):
        print(f'{self.name}: interaction completed')
        
class RectangleDisplay(Display): 
    
    
    def set_zone(self, zone: RectangleZone):
        self.zone = zone
    
    def draw(self, canvas):
        paint = canvas.paint
        
        paint.text_align = canvas.paint.TextAlign.CENTER
        paint.text_size = 36
        paint.color = "#b4b4b489"
        paint.style = Paint.Style.FILL
        r = self.zone.get_rect().center
        text = self.name
        tr = paint.measure_text(text)[1]
        
        canvas.draw_text(text,r.x+tr.center.x/2,r.y+tr.center.y/2)
        
        
        paint.color = "#b4b4b489"
        paint.style = Paint.Style.STROKE
        paint.stroke_width = 0.5
        canvas.draw_rect(self.zone.get_rect())
        pass