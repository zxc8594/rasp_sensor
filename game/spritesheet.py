import pygame

class spritesheet(object):
    def __init__(self, filename):
            self.sheet = pygame.image.load(filename).convert_alpha()
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle):
        "Loads image from x,y,x+offset,y+offset"
        #rect = pygame.Rect(rectangle)
        #image = pygame.Surface(rect.size).convert_alpha()
        #image.blit(self.sheet, (0, 0), rect)
        image_new = self.sheet.subsurface(rectangle)
        return image_new
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects):
        "Loads multiple images, supply a list of coordinates" 
        return [self.image_at(rect) for rect in rects]
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)
