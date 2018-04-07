
class Pancake:
    def __init__(self, r, h, top, surface):
        self.r = r
        self.h = h
        self.top = top
        self.surface = surface
        self.used = False
        self.top_surface = top + surface

    def set_used(self, used):
        self.used = used

    def is_used(self):
        return self.used

    def get_top_surace(self):
        return self.top_surface

    def sort_surface(self):
        return self.surface

