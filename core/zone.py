from talon.skia import Rect

class Zone:
    def contains_position(self, horizontal: int, vertical: int):
        pass

    def compute_interaction_value(self, horizontal: int, vertical: int):
        return None

class RectangleZone(Zone):
    def __init__(self, left: int, right: int, top: int, bottom: int) -> None:
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.rect = Rect(left,top,right-left,bottom-top)

    def contains_position(self, horizontal: int, vertical: int):
        return self.left < horizontal and self.right > horizontal and self.bottom > vertical and self.top < vertical
    
    def compute_interaction_value(self, horizontal: int, vertical: int):
        percentage_right = (horizontal - self.left)/(self.right - self.left)
        percentage_up = (self.bottom - vertical)/(self.bottom - self.top)
        value = RectangleInteractionValue(percentage_right, percentage_up)
        return value
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def get_top(self):
        return self.top
    
    def get_bottom(self):
        return self.bottom
    
    def get_rect(self):
        return self.rect
        
class RectangleInteractionValue:
    def __init__(self, percentage_right, percentage_up):
        self.percentage_right = percentage_right
        self.percentage_up = percentage_up
    
    def get_percentage_right(self):
        return self.percentage_right
    
    def get_percentage_up(self):
        return self.percentage_up