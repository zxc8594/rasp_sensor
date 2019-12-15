import pygame

class newsprite(object):
    def __init__(self, filename):
        self.img = pygame.image.load(filename).convert_alpha()
    def seperate(self, rectangle):
        new_img = img.subsurface((0,0,50,50))
        return new_img
        
    
