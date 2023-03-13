from .display import Display
from talon import ui, canvas

class DisplayDrawer:
    def __init__(self) -> None:
        self.displays = {}
        self.active = False
        
        # I am not sure about multiple screens here, but it could be theoretically supported
        screens = ui.screens()
        self.screen = screens[0]
        self.screenRect = self.screen.rect.copy()
        self.canvas = canvas.Canvas.from_screen(self.screen)
        pass
    
    def insert(self, display: Display, identifier: str) -> None:
        if identifier in self.displays:
            print(f"There is already a display with the identifier {identifier}")
            return
        
        self.displays[identifier] = display

    def enable(self) -> None:
        self.active = True
        self.canvas.register("draw", self.draw)
    
    def disable(self) -> None:
        self.active = False
        self.canvas.unregister("draw", self.draw) 
        
    def draw(self, canvas) -> None:
        if self.active==False:
            return
        
        for d in self.displays.values():
            d.draw(canvas)
        pass